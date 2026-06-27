#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import re
import shutil
import tempfile
import time
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Deque, Dict, Iterable, List, Optional, Tuple
from urllib.parse import urljoin, urlsplit, urlunsplit

import requests
from bs4 import BeautifulSoup

BASE_DOMAIN = "docs.gethealthie.com"
BASE_URL = f"https://{BASE_DOMAIN}"
SCRIPT_VERSION = "v1"
USER_AGENT = "healthie-documentation-mirror/1.0"
DEFAULT_SELECTED_REFERENCE_VERSION = "2026-01-01"

DEFAULT_SEED_URLS = [
    f"{BASE_URL}/",
    f"{BASE_URL}/guides/intro/",
    f"{BASE_URL}/guides/api-concepts/versioning/",
    f"{BASE_URL}/guides/api-concepts/changelog/",
]

REFERENCE_VERSION_RE = re.compile(r"^/reference/(\d{4}-\d{2}-\d{2})(?:/.*)?$")
VERSION_HEADING_RE = re.compile(r"^###\s+(\d{4}-\d{2}-\d{2})\s*$")
STANDARD_MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
AUTOLINK_RE = re.compile(r"(?<!\!)<((?:https?://|/)[^>]+)>")


@dataclass(frozen=True)
class Target:
    url: str
    normalized_url: str
    path: str
    accepted: bool
    section: Optional[str]
    reference_version: Optional[str]


@dataclass
class CrawlItem:
    target: Target
    depth: int
    source_type: str
    discovered_from: Optional[str]
    anchor_text: Optional[str]


class FatalSetupError(RuntimeError):
    pass


class SingleValueAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(namespace, self.dest, None) is not None:
            raise argparse.ArgumentError(self, f"{option_string} may only be provided once")
        setattr(namespace, self.dest, values)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_now_iso() -> str:
    return utc_now().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def strip_yaml_scalar(value: str) -> Optional[str]:
    stripped = value.strip()
    if not stripped:
        return None
    if (stripped.startswith('"') and stripped.endswith('"')) or (
        stripped.startswith("'") and stripped.endswith("'")
    ):
        return stripped[1:-1]
    return stripped


def parse_front_matter(markdown_text: str) -> Dict[str, object]:
    lines = markdown_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}

    result: Dict[str, object] = {}
    parent_key: Optional[str] = None
    for raw_line in lines[1:end_index]:
        if not raw_line.strip():
            continue
        if raw_line.startswith((" ", "\t")) and parent_key and isinstance(
            result.get(parent_key), dict
        ):
            nested = raw_line.strip()
            if ":" not in nested:
                continue
            nested_key, nested_value = nested.split(":", 1)
            result[parent_key][nested_key.strip()] = strip_yaml_scalar(nested_value)
            continue
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            result[key] = strip_yaml_scalar(value)
            parent_key = None
        else:
            result[key] = {}
            parent_key = key
    return result


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def path_without_query_or_fragment(url: str) -> str:
    parsed = urlsplit(url)
    return urlunsplit(("https", BASE_DOMAIN, parsed.path or "/", "", ""))


def normalize_path(path: str) -> Optional[str]:
    if not path:
        return "/"
    if "\x00" in path:
        return None
    if "//" in path and path != "/":
        return None

    parts = path.split("/")
    normalized_parts: List[str] = []
    for part in parts:
        if part in ("", "."):
            continue
        if part == "..":
            return None
        normalized_parts.append(part)

    if normalized_parts and normalized_parts[-1] in {"index", "index.md", "index.html"}:
        normalized_parts = normalized_parts[:-1]
    elif normalized_parts and re.search(r"\.(md|html)$", normalized_parts[-1]):
        return None

    if not normalized_parts:
        return "/"
    return "/" + "/".join(normalized_parts)


def classify_path(path: str) -> Tuple[bool, Optional[str], Optional[str]]:
    if path == "/guides" or path.startswith("/guides/"):
        return True, "guides", None
    if path == "/reference":
        return True, "reference", None
    version_match = REFERENCE_VERSION_RE.match(path)
    if version_match:
        return True, "reference", version_match.group(1)
    return False, None, None


def make_target(
    raw_url: str, *, base_url: Optional[str] = None, allow_root: bool = False
) -> Optional[Target]:
    cleaned = (raw_url or "").strip()
    if not cleaned:
        return None
    if cleaned.startswith("#") or cleaned.startswith("?"):
        return None
    if cleaned.startswith(("mailto:", "tel:")):
        return None

    absolute_url = urljoin(base_url or f"{BASE_URL}/", cleaned)
    parsed = urlsplit(absolute_url)
    if parsed.scheme not in ("http", "https"):
        return None

    hostname = (parsed.hostname or "").lower()
    if hostname != BASE_DOMAIN:
        return None

    if parsed.path.startswith("/_astro") or parsed.path.startswith("/explorer"):
        return None
    if parsed.path.startswith("/favicon"):
        return None

    normalized_path = normalize_path(parsed.path or "/")
    if normalized_path is None:
        return None

    accepted, section, reference_version = classify_path(normalized_path)
    if normalized_path == "/" and allow_root:
        accepted = False
        section = None
        reference_version = None
    elif not accepted:
        return None

    normalized_url = BASE_URL if normalized_path == "/" else f"{BASE_URL}{normalized_path}"
    raw_path = parsed.path or "/"
    cleaned_url = urlunsplit(("https", BASE_DOMAIN, raw_path, "", ""))
    return Target(
        url=cleaned_url,
        normalized_url=normalized_url,
        path=normalized_path,
        accepted=accepted,
        section=section,
        reference_version=reference_version,
    )


def target_html_url(target: Target) -> str:
    if target.path == "/":
        return f"{BASE_URL}/"
    return f"{target.normalized_url}/"


def target_markdown_url(target: Target) -> str:
    return f"{target.normalized_url}/index.md"


def target_relative_path(output_dir: Path, target: Target, suffix: str) -> Path:
    if target.section == "guides":
        base = output_dir / ("raw_html_fallback" if suffix == ".html" else "raw") / "guides"
        remainder = target.path[len("/guides") :].strip("/")
    elif target.section == "reference":
        base = output_dir / ("raw_html_fallback" if suffix == ".html" else "raw") / "reference"
        remainder = target.path[len("/reference") :].strip("/")
    else:
        raise ValueError(f"Unsupported target section for path mapping: {target.path}")

    if remainder:
        return base / remainder / f"index{suffix}"
    return base / f"index{suffix}"


def response_is_html(response: requests.Response) -> bool:
    content_type = response.headers.get("content-type", "").lower()
    text_sample = response.text[:500].lstrip().lower()
    return "html" in content_type or text_sample.startswith("<!doctype html") or text_sample.startswith("<html")


def looks_like_markdown(body: str) -> bool:
    stripped = body.lstrip()
    if not stripped:
        return False
    lowered = stripped[:500].lower()
    if lowered.startswith("<!doctype html") or lowered.startswith("<html"):
        return False
    if stripped.startswith("---\n"):
        return True
    patterns = (
        r"(?m)^#\s+\S+",
        r"(?m)^##\s+\S+",
        r"(?m)^\*\s+\S+",
        r"(?m)^-\s+\S+",
        r"(?m)^```",
        r"(?m)^\|.+\|$",
    )
    return any(re.search(pattern, stripped[:4000]) for pattern in patterns)


def response_is_markdown(response: requests.Response) -> bool:
    content_type = response.headers.get("content-type", "").lower()
    if "html" in content_type:
        return False
    if "markdown" in content_type:
        return True
    return looks_like_markdown(response.text)


def sanitize_html(html_text: str) -> str:
    soup = BeautifulSoup(html_text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    return soup.prettify()


def html_is_contentful(html_text: str) -> bool:
    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.get_text(" ", strip=True)
    return len(text) >= 120


def parse_version_candidates_from_markdown(markdown_text: str) -> List[str]:
    candidates: List[str] = []
    in_version_history = False
    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("## "):
            in_version_history = line.strip() == "## Version History (Breaking Changes)"
            continue
        if not in_version_history:
            continue
        match = VERSION_HEADING_RE.match(line.strip())
        if match:
            candidates.append(match.group(1))

    if "2024-06-01" in markdown_text and "2024-06-01" not in candidates:
        candidates.append("2024-06-01")
    return candidates


def write_jsonl_atomic(path: Path, rows: Iterable[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        temp_path = Path(handle.name)
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=True))
            handle.write("\n")
    shutil.move(str(temp_path), path)


def write_json_atomic(path: Path, payload: Dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        temp_path = Path(handle.name)
        json.dump(payload, handle, indent=2, ensure_ascii=True)
        handle.write("\n")
    shutil.move(str(temp_path), path)


def load_jsonl(path: Path) -> List[Dict[str, object]]:
    if not path.exists():
        return []
    rows: List[Dict[str, object]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped:
                continue
            rows.append(json.loads(stripped))
    return rows


class MirrorCrawler:
    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.selected_reference_version = args.reference_version
        self.reference_version_explicit = bool(args.reference_version_explicit)
        self.output_dir = Path(args.output_dir)
        self.raw_dir = self.output_dir / "raw"
        self.html_fallback_dir = self.output_dir / "raw_html_fallback"
        self.manifest_dir = self.output_dir / "manifest"
        self.indexes_dir = self.output_dir / "indexes"

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.last_request_at = 0.0

        self.logger = logging.getLogger("mirror_healthie_docs")
        self.started_at = utc_now()

        self.discovered_entries: Dict[str, Dict[str, object]] = {}
        self.downloaded_entries: Dict[str, Dict[str, object]] = {}
        self.failed_entries: List[Dict[str, object]] = []

        self.queue: Deque[CrawlItem] = deque()
        self.enqueued: Dict[str, CrawlItem] = {}
        self.visited_html: Dict[str, CrawlItem] = {}
        self.markdown_attempted: Dict[str, bool] = {}
        self.pending_downloads: Deque[CrawlItem] = deque()
        self.download_items: Dict[str, CrawlItem] = {}
        self.download_enqueued: Dict[str, bool] = {}
        self.html_contexts: Dict[str, Dict[str, object]] = {}

        self.pending_reference_urls: Dict[str, Dict[str, CrawlItem]] = defaultdict(dict)
        self.processed_reference_versions: Dict[str, bool] = {}
        self.validated_reference_versions: List[str] = []

        self.http_status_counts: Counter[str] = Counter()
        self.summary_counts: Counter[str] = Counter()

        self.previous_downloaded_by_source: Dict[str, Dict[str, object]] = {}
        self.previous_downloaded_by_slug: Dict[str, Dict[str, object]] = {}
        self.seed_urls = self.build_seed_urls()

    def build_seed_urls(self) -> List[str]:
        return list(DEFAULT_SEED_URLS) + [
            f"{BASE_URL}/reference/{self.selected_reference_version}/"
        ]

    def prepare_output_dirs(self) -> None:
        for path in (
            self.raw_dir / "guides",
            self.raw_dir / "reference",
            self.html_fallback_dir / "guides",
            self.html_fallback_dir / "reference",
            self.manifest_dir,
            self.indexes_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)

    def cleanup_stale_reference_artifacts(self) -> None:
        selected = self.selected_reference_version
        for root in (self.raw_dir / "reference", self.html_fallback_dir / "reference"):
            if not root.exists():
                continue
            for child in root.iterdir():
                if child.is_dir():
                    if child.name != selected:
                        shutil.rmtree(child)
                else:
                    child.unlink()

    def load_previous_manifests(self) -> None:
        previous_downloaded_path = self.manifest_dir / "downloaded_pages.jsonl"
        for row in load_jsonl(previous_downloaded_path):
            source_url = row.get("source_url")
            slug = row.get("slug")
            if isinstance(source_url, str):
                self.previous_downloaded_by_source[source_url] = row
            if isinstance(slug, str):
                self.previous_downloaded_by_slug[slug] = row

    def throttled_get(self, url: str) -> requests.Response:
        attempts = 0
        while True:
            elapsed = time.monotonic() - self.last_request_at
            if elapsed < self.args.delay_seconds:
                time.sleep(self.args.delay_seconds - elapsed)

            self.last_request_at = time.monotonic()
            try:
                response = self.session.get(url, timeout=self.args.timeout, allow_redirects=True)
            except requests.RequestException:
                attempts += 1
                if attempts > 2:
                    raise
                time.sleep(self.args.delay_seconds * (attempts + 1))
                continue
            self.http_status_counts[str(response.status_code)] += 1

            if response.status_code == 429 or 500 <= response.status_code < 600:
                attempts += 1
                if attempts > 2:
                    return response
                retry_after = response.headers.get("Retry-After")
                delay_seconds = self.args.delay_seconds * (attempts + 1)
                if retry_after and retry_after.isdigit():
                    delay_seconds = max(delay_seconds, float(retry_after))
                self.logger.warning(
                    "Retrying %s after HTTP %s (attempt %s/2)",
                    url,
                    response.status_code,
                    attempts,
                )
                time.sleep(delay_seconds)
                continue
            return response

    def record_failure(
        self,
        *,
        source_url: str,
        markdown_url: Optional[str],
        http_status: Optional[int],
        content_type: Optional[str],
        error_type: str,
        error: str,
        discovered_from: Optional[str],
        section: Optional[str],
        reference_version: Optional[str],
        fallback_used: Optional[str],
        retryable: bool,
        final_source_url: Optional[str] = None,
    ) -> None:
        self.failed_entries.append(
            {
                "source_url": source_url,
                "final_source_url": final_source_url,
                "markdown_url": markdown_url,
                "http_status": http_status,
                "content_type": content_type,
                "error_type": error_type,
                "error": error,
                "discovered_from": discovered_from,
                "section": section,
                "reference_version": reference_version,
                "fallback_used": fallback_used,
                "retryable": retryable,
                "failed_at": utc_now_iso(),
            }
        )

    def enqueue_item(self, item: CrawlItem) -> None:
        key = item.target.normalized_url
        if key in self.visited_html or key in self.enqueued:
            return
        self.queue.append(item)
        self.enqueued[key] = item

    def enqueue_download(self, item: CrawlItem) -> None:
        key = item.target.normalized_url
        if key in self.download_items:
            return
        self.download_items[key] = item
        self.pending_downloads.append(item)
        self.download_enqueued[key] = True

    def record_discovered(self, item: CrawlItem) -> None:
        if not item.target.accepted:
            return
        key = item.target.normalized_url
        if key in self.discovered_entries:
            return
        self.discovered_entries[key] = {
            "url": item.target.url,
            "normalized_url": item.target.normalized_url,
            "path": item.target.path,
            "section": item.target.section,
            "reference_version": item.target.reference_version,
            "source_type": item.source_type,
            "discovered_from": item.discovered_from,
            "anchor_text": item.anchor_text,
            "depth": item.depth,
            "first_seen_at": utc_now_iso(),
        }

    def should_crawl_html(self, target: Target) -> bool:
        if target.path == "/":
            return True
        if target.section == "guides":
            return True
        if (
            target.section == "reference"
            and target.reference_version
            and target.reference_version == self.selected_reference_version
            and target.path == f"/reference/{target.reference_version}"
        ):
            return True
        return False

    def reference_version_allowed(self, version: Optional[str]) -> bool:
        if not version:
            return True
        return version == self.selected_reference_version

    def normalize_discovered_url(self, raw_url: str, *, base_url: Optional[str]) -> str:
        absolute_url = urljoin(base_url or f"{BASE_URL}/", raw_url)
        parsed = urlsplit(absolute_url)
        if (parsed.hostname or "").lower() != BASE_DOMAIN:
            return absolute_url

        normalized_path = normalize_path(parsed.path or "/")
        if normalized_path == "/reference":
            return f"{BASE_URL}/reference/{self.selected_reference_version}/"
        return absolute_url

    def queue_target(
        self,
        raw_url: str,
        *,
        base_url: Optional[str],
        source_type: str,
        discovered_from: Optional[str],
        anchor_text: Optional[str],
        depth: int,
        allow_root: bool = False,
    ) -> None:
        normalized_raw_url = self.normalize_discovered_url(raw_url, base_url=base_url)
        target = make_target(normalized_raw_url, base_url=None, allow_root=allow_root)
        if not target:
            return
        if target.reference_version and not self.reference_version_allowed(target.reference_version):
            return

        item = CrawlItem(
            target=target,
            depth=depth,
            source_type=source_type,
            discovered_from=discovered_from,
            anchor_text=anchor_text,
        )
        self.record_discovered(item)

        if target.reference_version and target.reference_version not in self.validated_reference_versions:
            self.pending_reference_urls[target.reference_version][target.normalized_url] = item
            self.register_reference_version_candidate(
                target.reference_version,
                discovered_from=discovered_from or target.normalized_url,
                depth=depth,
            )
            return

        if target.accepted:
            self.enqueue_download(item)
        if self.should_crawl_html(target):
            self.enqueue_item(item)

    def register_reference_version_candidate(
        self, version: str, *, discovered_from: Optional[str], depth: int
    ) -> None:
        if not self.reference_version_allowed(version):
            return

        candidate_url = f"{BASE_URL}/reference/{version}/"
        target = make_target(candidate_url, allow_root=False)
        if not target:
            return

        candidate_item = CrawlItem(
            target=target,
            depth=depth,
            source_type="version_candidate",
            discovered_from=discovered_from,
            anchor_text=None,
        )
        self.record_discovered(candidate_item)
        self.pending_reference_urls[version][target.normalized_url] = candidate_item

        if self.processed_reference_versions.get(version):
            return
        self.processed_reference_versions[version] = True

        markdown_url = target_markdown_url(target)
        self.logger.info("Validating reference version %s", version)
        try:
            response = self.throttled_get(markdown_url)
        except requests.RequestException as exc:
            if version == self.selected_reference_version:
                raise FatalSetupError(
                    f"Selected reference version {version} could not be validated: {exc}"
                ) from exc
            self.record_failure(
                source_url=target.normalized_url,
                markdown_url=markdown_url,
                http_status=None,
                content_type=None,
                error_type="reference_version_not_available",
                error=str(exc),
                discovered_from=discovered_from,
                section="reference",
                reference_version=version,
                fallback_used=None,
                retryable=True,
            )
            self.pending_reference_urls.pop(version, None)
            return

        if response.status_code == 200 and response_is_markdown(response):
            if version not in self.validated_reference_versions:
                self.validated_reference_versions.append(version)
            for pending_item in self.pending_reference_urls.pop(version, {}).values():
                self.enqueue_download(pending_item)
                if self.should_crawl_html(pending_item.target):
                    self.enqueue_item(pending_item)
            final_target = make_target(
                path_without_query_or_fragment(response.url), allow_root=False
            )
            if (
                final_target
                and final_target.accepted
                and final_target.normalized_url != target.normalized_url
            ):
                self.queue_target(
                    final_target.url,
                    base_url=None,
                    source_type="redirect",
                    discovered_from=target.normalized_url,
                    anchor_text=None,
                    depth=depth,
                )
            return

        if version == self.selected_reference_version:
            raise FatalSetupError(
                f"Selected reference version {version} did not expose a valid index.md"
            )

        self.record_failure(
            source_url=target.normalized_url,
            markdown_url=markdown_url,
            http_status=response.status_code,
            content_type=response.headers.get("content-type"),
            error_type="reference_version_not_available",
            error="Reference version candidate did not expose index.md",
            discovered_from=discovered_from,
            section="reference",
            reference_version=version,
            fallback_used=None,
            retryable=response.status_code in {429, 500, 502, 503, 504},
        )
        self.pending_reference_urls.pop(version, None)

    def extract_html_links(self, html: str, *, base_url: str) -> List[Tuple[str, Optional[str]]]:
        soup = BeautifulSoup(html, "html.parser")
        discovered: List[Tuple[str, Optional[str]]] = []
        for anchor in soup.find_all("a", href=True):
            href = anchor.get("href")
            if not href:
                continue
            anchor_text = anchor.get_text(" ", strip=True) or None
            discovered.append((urljoin(base_url, href), anchor_text))
        return discovered

    def extract_markdown_links(
        self, markdown_text: str, *, base_url: str
    ) -> List[Tuple[str, Optional[str]]]:
        discovered: List[Tuple[str, Optional[str]]] = []
        for match in STANDARD_MARKDOWN_LINK_RE.finditer(markdown_text):
            label = match.group(1).strip() or None
            href = match.group(2).strip()
            discovered.append((urljoin(base_url, href), label))
        for match in AUTOLINK_RE.finditer(markdown_text):
            discovered.append((urljoin(base_url, match.group(1).strip()), None))
        return discovered

    def read_existing_markdown_entry(
        self, item: CrawlItem, local_path: Path
    ) -> Tuple[Dict[str, object], str]:
        text = local_path.read_text(encoding="utf-8")
        front_matter = parse_front_matter(text)
        sha256 = sha256_text(text)
        bytes_count = len(text.encode("utf-8"))
        previous = self.previous_downloaded_by_source.get(item.target.normalized_url) or self.previous_downloaded_by_slug.get(
            item.target.path
        )
        local_path_text = local_path.as_posix()
        if previous:
            entry = dict(previous)
            entry["local_path"] = local_path_text
            entry["skipped_existing"] = True
            entry.setdefault("source_url", item.target.normalized_url)
            entry.setdefault("final_source_url", item.target.normalized_url)
            entry.setdefault("markdown_url", target_markdown_url(item.target))
            entry.setdefault("final_markdown_url", target_markdown_url(item.target))
            entry.setdefault("title", front_matter.get("title"))
            entry.setdefault("description", front_matter.get("description"))
            entry.setdefault("section", item.target.section)
            entry.setdefault("reference_version", item.target.reference_version)
            entry.setdefault("slug", item.target.path)
            entry["sha256"] = sha256
            entry["bytes"] = bytes_count
            return entry, text

        source_url_value = front_matter.get("source_url")
        final_source_url = item.target.normalized_url
        final_markdown_url = target_markdown_url(item.target)
        if isinstance(source_url_value, dict):
            html_source = source_url_value.get("html")
            markdown_source = source_url_value.get("md")
            if isinstance(html_source, str):
                final_source_url = html_source.removesuffix("/index")
            if isinstance(markdown_source, str):
                final_markdown_url = markdown_source

        return {
            "source_url": item.target.normalized_url,
            "final_source_url": final_source_url,
            "markdown_url": target_markdown_url(item.target),
            "final_markdown_url": final_markdown_url,
            "local_path": local_path_text,
            "http_status": 200,
            "content_type": "text/markdown",
            "title": front_matter.get("title"),
            "description": front_matter.get("description"),
            "section": item.target.section,
            "reference_version": item.target.reference_version,
            "slug": item.target.path,
            "sha256": sha256,
            "bytes": bytes_count,
            "skipped_existing": True,
            "fetched_at": utc_now_iso(),
        }, text

    def persist_markdown(
        self,
        item: CrawlItem,
        markdown_text: str,
        response: requests.Response,
        *,
        final_source_url: Optional[str],
    ) -> Dict[str, object]:
        local_path = target_relative_path(self.output_dir, item.target, ".md")
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_text(markdown_text, encoding="utf-8")

        front_matter = parse_front_matter(markdown_text)
        source_url_value = front_matter.get("source_url")
        final_markdown_url = path_without_query_or_fragment(response.url)
        front_matter_source_url = None
        if isinstance(source_url_value, dict):
            html_source = source_url_value.get("html")
            markdown_source = source_url_value.get("md")
            if isinstance(html_source, str):
                front_matter_source_url = html_source.removesuffix("/index")
            if isinstance(markdown_source, str):
                final_markdown_url = markdown_source

        entry = {
            "source_url": item.target.normalized_url,
            "final_source_url": final_source_url or front_matter_source_url or item.target.normalized_url,
            "markdown_url": target_markdown_url(item.target),
            "final_markdown_url": final_markdown_url,
            "local_path": local_path.as_posix(),
            "http_status": response.status_code,
            "content_type": response.headers.get("content-type"),
            "title": front_matter.get("title"),
            "description": front_matter.get("description"),
            "section": item.target.section,
            "reference_version": item.target.reference_version,
            "slug": item.target.path,
            "sha256": sha256_text(markdown_text),
            "bytes": len(markdown_text.encode("utf-8")),
            "skipped_existing": False,
            "fetched_at": utc_now_iso(),
        }
        return entry

    def save_html_fallback(self, item: CrawlItem, html_text: str) -> Optional[str]:
        if item.target.path == "/reference":
            return None
        if item.target.reference_version and not self.reference_version_allowed(
            item.target.reference_version
        ):
            return None
        if not self.args.save_html_fallback:
            return None
        if not html_is_contentful(html_text):
            return None
        local_path = target_relative_path(self.output_dir, item.target, ".html")
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_text(sanitize_html(html_text), encoding="utf-8")
        self.summary_counts["html_fallback_pages"] += 1
        return "html_saved"

    def handle_markdown(
        self,
        item: CrawlItem,
        *,
        final_source_url: Optional[str],
        html_status: Optional[int],
        html_content_type: Optional[str],
        html_text: Optional[str],
        html_links_found: bool,
    ) -> None:
        if self.markdown_attempted.get(item.target.normalized_url):
            return
        if (
            self.args.max_pages
            and self.summary_counts["markdown_pages_processed"] >= self.args.max_pages
        ):
            return
        self.markdown_attempted[item.target.normalized_url] = True
        self.summary_counts["markdown_pages_processed"] += 1

        local_path = target_relative_path(self.output_dir, item.target, ".md")
        if local_path.exists() and not self.args.refresh:
            entry, markdown_text = self.read_existing_markdown_entry(item, local_path)
            self.summary_counts["skipped_existing"] += 1
            self.downloaded_entries[item.target.normalized_url] = entry
            self.discover_from_markdown(item, markdown_text)
            return

        markdown_url = target_markdown_url(item.target)
        try:
            response = self.throttled_get(markdown_url)
        except requests.RequestException as exc:
            fallback_used = None
            if html_status == 200 and html_text and html_links_found:
                fallback_used = self.save_html_fallback(item, html_text) or "html_links_only"
            self.record_failure(
                source_url=item.target.normalized_url,
                markdown_url=markdown_url,
                http_status=None,
                content_type=None,
                error_type="markdown_request_failed",
                error=str(exc),
                discovered_from=item.discovered_from,
                section=item.target.section,
                reference_version=item.target.reference_version,
                fallback_used=fallback_used,
                retryable=True,
                final_source_url=final_source_url,
            )
            return

        if response.status_code == 200 and response_is_markdown(response):
            markdown_text = response.text
            final_markdown_target = make_target(
                response.url.replace("/index.md", "/"), allow_root=False
            )
            if (
                final_markdown_target
                and final_markdown_target.accepted
                and final_markdown_target.normalized_url != item.target.normalized_url
            ):
                self.queue_target(
                    final_markdown_target.url,
                    base_url=None,
                    source_type="redirect",
                    discovered_from=item.target.normalized_url,
                    anchor_text=None,
                    depth=item.depth,
                )

            entry = self.persist_markdown(
                item,
                markdown_text,
                response,
                final_source_url=final_source_url,
            )
            self.downloaded_entries[item.target.normalized_url] = entry
            self.discover_from_markdown(item, markdown_text)
            return

        fallback_used = None
        if html_status == 200 and html_text and html_links_found:
            fallback_used = self.save_html_fallback(item, html_text) or "html_links_only"

        if response.status_code == 404:
            error_type = "markdown_not_available"
            error = "Markdown page was not available at index.md"
        elif response.status_code == 200 and response_is_html(response):
            error_type = "markdown_response_was_html"
            error = "Markdown URL returned HTML content instead of Markdown"
        else:
            error_type = "markdown_download_failed"
            error = "Markdown URL did not return usable Markdown content"

        self.record_failure(
            source_url=item.target.normalized_url,
            markdown_url=markdown_url,
            http_status=response.status_code,
            content_type=response.headers.get("content-type"),
            error_type=error_type,
            error=error,
            discovered_from=item.discovered_from,
            section=item.target.section,
            reference_version=item.target.reference_version,
            fallback_used=fallback_used,
            retryable=response.status_code in {429, 500, 502, 503, 504},
            final_source_url=final_source_url,
        )

    def discover_from_markdown(self, item: CrawlItem, markdown_text: str) -> None:
        if item.target.path == "/guides/api-concepts/versioning":
            candidates = parse_version_candidates_from_markdown(markdown_text)
            if (
                not self.reference_version_explicit
                and self.selected_reference_version not in candidates
            ):
                raise FatalSetupError(
                    f"Selected reference version {self.selected_reference_version} was not listed in the versioning guide"
                )
            self.register_reference_version_candidate(
                self.selected_reference_version,
                discovered_from=item.target.normalized_url,
                depth=item.depth + 1,
            )

        for url, anchor_text in self.extract_markdown_links(
            markdown_text, base_url=item.target.normalized_url + "/"
        ):
            self.queue_target(
                url,
                base_url=None,
                source_type="markdown_link",
                discovered_from=item.target.normalized_url,
                anchor_text=anchor_text,
                depth=item.depth + 1,
            )

    def crawl(self) -> None:
        self.prepare_output_dirs()
        self.cleanup_stale_reference_artifacts()
        self.load_previous_manifests()

        for seed_url in self.seed_urls:
            self.queue_target(
                seed_url,
                base_url=None,
                source_type="seed",
                discovered_from=None,
                anchor_text=None,
                depth=0,
                allow_root=seed_url == f"{BASE_URL}/",
            )

        # The home page seed is intentionally fetched for discovery even though it is outside
        # the accepted manifest scope.
        home_target = make_target(f"{BASE_URL}/", allow_root=True)
        if home_target:
            self.enqueue_item(
                CrawlItem(
                    target=home_target,
                    depth=0,
                    source_type="seed",
                    discovered_from=None,
                    anchor_text=None,
                )
            )

        while self.queue or self.pending_downloads:
            if self.queue:
                if self.args.max_pages and self.summary_counts["html_pages_visited"] >= self.args.max_pages:
                    self.logger.warning(
                        "Reached --max-pages=%s; stopping crawl loop",
                        self.args.max_pages,
                    )
                    self.queue.clear()
                else:
                    item = self.queue.popleft()
                    self.enqueued.pop(item.target.normalized_url, None)

                    if item.target.normalized_url in self.visited_html:
                        continue

                    self.visited_html[item.target.normalized_url] = item
                    self.summary_counts["html_pages_visited"] += 1
                    self.logger.info("Crawling HTML %s", item.target.normalized_url)

                    html_status = None
                    html_content_type = None
                    html_text = None
                    html_links_found = False
                    final_source_url = item.target.normalized_url if item.target.accepted else None

                    try:
                        response = self.throttled_get(target_html_url(item.target))
                    except requests.RequestException as exc:
                        self.logger.warning(
                            "HTML fetch failed for %s: %s",
                            item.target.normalized_url,
                            exc,
                        )
                        response = None
                        if item.target.accepted:
                            self.record_failure(
                                source_url=item.target.normalized_url,
                                markdown_url=None,
                                http_status=None,
                                content_type=None,
                                error_type="html_request_failed",
                                error=str(exc),
                                discovered_from=item.discovered_from,
                                section=item.target.section,
                                reference_version=item.target.reference_version,
                                fallback_used=None,
                                retryable=True,
                            )

                    if response is not None:
                        html_status = response.status_code
                        html_content_type = response.headers.get("content-type")
                        final_target = make_target(
                            path_without_query_or_fragment(response.url),
                            allow_root=item.target.path == "/",
                        )
                        if final_target and final_target.accepted:
                            final_source_url = final_target.normalized_url
                            if final_target.normalized_url != item.target.normalized_url:
                                self.queue_target(
                                    final_target.url,
                                    base_url=None,
                                    source_type="redirect",
                                    discovered_from=item.target.normalized_url,
                                    anchor_text=None,
                                    depth=item.depth,
                                )

                        if response.status_code == 200 and response_is_html(response):
                            html_text = response.text
                            html_links = self.extract_html_links(html_text, base_url=response.url)
                            html_links_found = bool(html_links)
                            for url, anchor_text in html_links:
                                self.queue_target(
                                    url,
                                    base_url=None,
                                    source_type="html_link",
                                    discovered_from=final_source_url or item.target.normalized_url,
                                    anchor_text=anchor_text,
                                    depth=item.depth + 1,
                                )

                    if item.target.accepted:
                        self.html_contexts[item.target.normalized_url] = {
                            "final_source_url": final_source_url,
                            "html_status": html_status,
                            "html_content_type": html_content_type,
                            "html_text": html_text,
                            "html_links_found": html_links_found,
                        }
                        self.handle_markdown(
                            item,
                            final_source_url=final_source_url,
                            html_status=html_status,
                            html_content_type=html_content_type,
                            html_text=html_text,
                            html_links_found=html_links_found,
                        )
                    continue

            download_item = self.pending_downloads.popleft()
            if (
                self.args.max_pages
                and self.summary_counts["markdown_pages_processed"] >= self.args.max_pages
            ):
                self.pending_downloads.clear()
                continue
            context = self.html_contexts.get(download_item.target.normalized_url, {})
            self.handle_markdown(
                download_item,
                final_source_url=context.get("final_source_url"),
                html_status=context.get("html_status"),
                html_content_type=context.get("html_content_type"),
                html_text=context.get("html_text"),
                html_links_found=bool(context.get("html_links_found")),
            )

        self.summary_counts["discovered_urls"] = len(self.discovered_entries)
        self.summary_counts["downloaded_pages"] = len(self.downloaded_entries)
        self.summary_counts["failed_urls"] = len(self.failed_entries)

        self.write_manifests()

    def downloaded_records_for_index(self) -> List[Dict[str, object]]:
        if self.downloaded_entries:
            rows = list(self.downloaded_entries.values())
        else:
            rows = load_jsonl(self.manifest_dir / "downloaded_pages.jsonl")
        return sorted(
            rows,
            key=lambda row: (
                row.get("section") or "",
                row.get("reference_version") or "",
                row.get("slug") or "",
            ),
        )

    def build_indexes(self) -> None:
        rows = self.downloaded_records_for_index()
        if not rows:
            raise FatalSetupError("Index generation requires downloaded pages; none were found.")

        generated_at = utc_now_iso()
        sitemap_json = {
            "generated_at": generated_at,
            "pages": [
                {
                    "title": row.get("title") or row.get("slug"),
                    "section": row.get("section"),
                    "reference_version": row.get("reference_version"),
                    "slug": row.get("slug"),
                    "source_url": row.get("source_url"),
                    "markdown_url": row.get("markdown_url"),
                    "local_path": row.get("local_path"),
                }
                for row in rows
            ],
        }
        write_json_atomic(self.indexes_dir / "sitemap.json", sitemap_json)

        guides = [row for row in rows if row.get("section") == "guides"]
        references = [row for row in rows if row.get("section") == "reference"]

        lines = [
            "# Healthie Docs Sitemap",
            "",
            f"Generated at: {generated_at}",
            "",
            "## How to search",
            "",
            "- `rg \"AuthorizationSource\" healthie_docs/raw`",
            "- `rg \"Healthie-GraphQL-API-Version\" healthie_docs/raw`",
            "- `rg \"webhook\" healthie_docs/raw/guides`",
            "",
            "## Guides",
            "",
        ]

        if guides:
            for row in sorted(guides, key=lambda record: str(record.get("slug") or "")):
                link_path = Path(str(row["local_path"])).relative_to(self.output_dir)
                relative_link = Path("..") / link_path
                title = row.get("title") or row.get("slug")
                lines.append(
                    f"- [{title}]({relative_link.as_posix()}) - `{row.get('slug')}` - Source: {row.get('source_url')}"
                )
        else:
            lines.append("- None")

        lines.extend(["", "## Reference", ""])
        if references:
            grouped: Dict[str, List[Dict[str, object]]] = defaultdict(list)
            for row in references:
                version = str(row.get("reference_version") or "unknown")
                grouped[version].append(row)

            for version in sorted(grouped):
                lines.append(f"### {version}")
                lines.append("")
                for row in sorted(grouped[version], key=lambda record: str(record.get("slug") or "")):
                    link_path = Path(str(row["local_path"])).relative_to(self.output_dir)
                    relative_link = Path("..") / link_path
                    title = row.get("title") or row.get("slug")
                    lines.append(
                        f"- [{title}]({relative_link.as_posix()}) - `{row.get('slug')}` - Source: {row.get('source_url')}"
                    )
                lines.append("")
        else:
            lines.append("- None")

        sitemap_md = "\n".join(lines).rstrip() + "\n"
        self.indexes_dir.mkdir(parents=True, exist_ok=True)
        (self.indexes_dir / "sitemap.md").write_text(sitemap_md, encoding="utf-8")

    def build_summary(self) -> Dict[str, object]:
        sections = Counter()
        for row in self.downloaded_entries.values():
            section = row.get("section")
            if isinstance(section, str):
                sections[section] += 1

        return {
            "started_at": self.started_at.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "finished_at": utc_now_iso(),
            "duration_seconds": int((utc_now() - self.started_at).total_seconds()),
            "base_domain": BASE_DOMAIN,
            "mode": self.args.mode,
            "refresh": self.args.refresh,
            "seed_urls": self.seed_urls,
            "selected_reference_version": self.selected_reference_version,
            "validated_reference_versions": sorted(self.validated_reference_versions),
            "counts": {
                "discovered_urls": int(self.summary_counts["discovered_urls"]),
                "html_pages_visited": int(self.summary_counts["html_pages_visited"]),
                "downloaded_pages": int(self.summary_counts["downloaded_pages"]),
                "skipped_existing": int(self.summary_counts["skipped_existing"]),
                "failed_urls": int(self.summary_counts["failed_urls"]),
                "html_fallback_pages": int(self.summary_counts["html_fallback_pages"]),
            },
            "http_status_counts": dict(sorted(self.http_status_counts.items())),
            "sections": {
                "guides": int(sections["guides"]),
                "reference": int(sections["reference"]),
            },
            "output_dir": self.output_dir.as_posix(),
            "script_version": SCRIPT_VERSION,
        }

    def write_manifests(self) -> None:
        write_jsonl_atomic(
            self.manifest_dir / "discovered_urls.jsonl",
            list(self.discovered_entries.values()),
        )
        write_jsonl_atomic(
            self.manifest_dir / "downloaded_pages.jsonl",
            list(self.downloaded_entries.values()),
        )
        write_jsonl_atomic(self.manifest_dir / "failed_urls.jsonl", self.failed_entries)
        write_json_atomic(self.manifest_dir / "crawl_summary.json", self.build_summary())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mirror the public Healthie documentation into local Markdown files."
    )
    parser.add_argument("--mode", choices=("crawl", "index", "all"), required=True)
    parser.add_argument("--output-dir", default="healthie_docs")
    parser.add_argument("--refresh", action="store_true", help="Re-download existing Markdown files.")
    parser.add_argument("--timeout", type=float, default=30)
    parser.add_argument("--delay-seconds", type=float, default=0.2)
    parser.add_argument("--max-pages", type=int)
    parser.add_argument(
        "--reference-version",
        action=SingleValueAction,
        default=None,
        help=f"Single reference version override. Defaults to {DEFAULT_SELECTED_REFERENCE_VERSION}.",
    )
    parser.add_argument(
        "--save-html-fallback",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Save sanitized HTML fallbacks when Markdown is unavailable.",
    )
    parser.add_argument("--log-level", default="INFO")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.reference_version_explicit = args.reference_version is not None
    if args.reference_version is None:
        args.reference_version = DEFAULT_SELECTED_REFERENCE_VERSION

    logging.basicConfig(
        level=getattr(logging, str(args.log_level).upper(), logging.INFO),
        format="%(asctime)s %(levelname)s %(message)s",
    )

    crawler = MirrorCrawler(args)
    try:
        if args.mode in {"crawl", "all"}:
            crawler.crawl()
            if not crawler.downloaded_entries:
                raise FatalSetupError("Crawl completed with zero downloaded pages.")
        if args.mode in {"index", "all"}:
            crawler.build_indexes()
            if not crawler.downloaded_records_for_index():
                raise FatalSetupError("Index generation completed with zero indexed pages.")
    except FatalSetupError as exc:
        logging.error("%s", exc)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
