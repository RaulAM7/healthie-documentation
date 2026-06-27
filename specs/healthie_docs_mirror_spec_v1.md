# Healthie Documentation Mirror Spec v1 - Latest Reference Only

## Objective

Build a local, re-runnable mirror of the public Healthie documentation for EPI10 Salud technical research.

The mirror is intentionally latest-reference-only: mirror all public guides, but mirror only the latest live Healthie reference version used for current development.

The mirror must include, at minimum:

- Public docs under `https://docs.gethealthie.com/guides/`
- Public docs under the selected latest reference version, currently `https://docs.gethealthie.com/reference/2026-01-01/`
- No local mirror of older reference versions unless a future spec explicitly changes this
- Markdown pages available through `<slug>/index.md`
- A discovered URL manifest
- A downloaded pages manifest
- A failed URLs manifest
- A crawl summary
- A local navigable index
- README usage documentation

This phase is only for mirroring public documentation. It must not implement any Healthie integration or EPI10 functional research.

## Planning Observations

These observations were validated during planning on 2026-06-27 with limited HTTP checks, not a mass crawl:

- `https://docs.gethealthie.com/guides/intro/index.md` returned `200` with `text/markdown`.
- `https://docs.gethealthie.com/guides/api-concepts/authentication/index.md` returned `200` with `text/markdown`.
- `https://docs.gethealthie.com/reference/2024-06-01/enums/action/index.md` returned `200` with `text/markdown`.
- `https://docs.gethealthie.com/reference/` redirected to `/reference/2024-10-20` during planning, but the versioning guide mentioned newer versions. Do not use unversioned `/reference` as a crawl seed for latest-only mode.
- `https://docs.gethealthie.com/sitemap.xml`, `https://docs.gethealthie.com/robots.txt`, `https://docs.gethealthie.com/index.md`, and `https://docs.gethealthie.com/guides/index.md` did not provide useful crawl entrypoints during planning.
- `/guides/intro/` contained the guides navigation links.
- `/reference/<version>/` contained reference navigation links for that version.
- The versioning guide included date strings that are not necessarily available reference versions. Do not treat every date as a crawl target; validate only the selected live reference version.
- Healthie Markdown pages observed during planning included YAML front matter with fields like `title` and `source_url`.
- As of 2026-06-27, the latest published reference version visible in the versioning guide is `2026-01-01`.
- `https://docs.gethealthie.com/reference/2026-01-01/index.md` returned `200` with `text/markdown` during review.
- `https://docs.gethealthie.com/reference/2026-07-01/index.md` returned `404` during review; that date appears in lifecycle policy text, not as a published reference tree yet.

## Scope And Limits

In scope:

- Create `scripts/mirror_healthie_docs.py`.
- Create/update `requirements.txt` with Python dependencies.
- Create `healthie_docs/` output structure.
- Crawl public Healthie documentation from static HTML links.
- Download Markdown pages using `/index.md`.
- Generate JSONL manifests and local indexes.
- Update root `README.md` with mirror usage instructions.
- Run one complete latest-only public-doc mirror after implementation.

Out of scope:

- No Healthie API keys.
- No authenticated endpoints.
- No calls to real customer, patient, provider, or EPI10 data.
- No Healthie integration implementation.
- No functional research for EPI10 workflows.
- No private scraping.
- No local mirror of non-latest reference versions.
- No use of `agent-browser` as the first option.
- `agent-browser` may only be mentioned as an optional fallback if static crawling misses navigation that cannot be recovered from HTML.

## Target Structure

Create this structure:

```text
healthie_docs/
  raw/
    guides/
    reference/
      2026-01-01/
  raw_html_fallback/
    guides/
    reference/
  manifest/
    discovered_urls.jsonl
    downloaded_pages.jsonl
    failed_urls.jsonl
    crawl_summary.json
  indexes/
    sitemap.md
    sitemap.json
scripts/
  mirror_healthie_docs.py
requirements.txt
specs/
  healthie_docs_mirror_spec_v1.md
README.md
```

Path mapping rules:

- `/guides/intro/` -> `healthie_docs/raw/guides/intro/index.md`
- `/guides/api-concepts/authentication/` -> `healthie_docs/raw/guides/api-concepts/authentication/index.md`
- `/reference/2026-01-01/enums/action` -> `healthie_docs/raw/reference/2026-01-01/enums/action/index.md`
- HTML fallback, only when needed, mirrors the same path under `healthie_docs/raw_html_fallback/`.

## Implementation Requirements

Use Python 3 with:

- `requests`
- `beautifulsoup4`
- `pathlib`
- standard-library `json`, `hashlib`, `argparse`, `datetime`, `time`, `re`, `tempfile`, `shutil`, and `urllib.parse`

Create `requirements.txt`:

```text
requests>=2.31.0
beautifulsoup4>=4.12.0
```

Required CLI examples:

```bash
python scripts/mirror_healthie_docs.py --mode crawl
python scripts/mirror_healthie_docs.py --mode crawl --refresh
python scripts/mirror_healthie_docs.py --mode index
python scripts/mirror_healthie_docs.py --mode all
python scripts/mirror_healthie_docs.py --mode all --reference-version 2026-01-01
```

Required CLI arguments:

- `--mode {crawl,index,all}`
- `--output-dir healthie_docs`, default `healthie_docs`
- `--refresh`, default false
- `--timeout`, default `30`
- `--delay-seconds`, default `0.2`
- `--max-pages`, optional smoke-test limit
- `--reference-version`, optional single selected reference version override, default `2026-01-01`
- `--save-html-fallback`, default true
- `--log-level`, default `INFO`

Behavior:

- Idempotent and re-runnable.
- Do not duplicate manifest rows on rerun.
- Rebuild manifests per run by writing temporary files and atomically replacing the old manifests.
- Skip existing Markdown files unless `--refresh` is set.
- Preserve prior manifest metadata for skipped files when possible.
- Continue after individual 404s, redirects, timeouts, and parse failures.
- Exit non-zero only on fatal setup errors or if crawl completes with zero downloaded or indexed pages.
- Default behavior must be latest-only. Running `python scripts/mirror_healthie_docs.py --mode all` must not mirror older reference versions.
- `--reference-version` is an explicit override for the selected live version. It must not be repeatable in v1.
- Older reference folders under `healthie_docs/raw/reference/` must be removed or ignored so stale versions cannot appear in manifests or indexes.

## Crawling Strategy

Base domain:

- Only crawl `https://docs.gethealthie.com`.

Initial seed URLs:

- `https://docs.gethealthie.com/`
- `https://docs.gethealthie.com/guides/intro/`
- `https://docs.gethealthie.com/guides/api-concepts/versioning/`
- `https://docs.gethealthie.com/guides/api-concepts/changelog/`
- `https://docs.gethealthie.com/reference/2026-01-01/`

Do not seed unversioned `/reference/`, because it redirects to an older version and creates stale latest-only artifacts.

URL filters:

- Accept only same-domain URLs.
- Accept only paths under:
  - `/guides`
  - `/guides/`
- Accept `/reference/<selected_reference_version>`
- Accept `/reference/<selected_reference_version>/...`
- Ignore:
  - unversioned `/reference`
  - `/reference/<non_selected_version>`
  - `/explorer`
  - `/_astro`
  - `/favicon`
  - external links
  - `mailto:`
  - `tel:`
  - pure fragment links
  - query-only variants

Normalization:

- Resolve relative links with `urljoin`.
- Strip query and fragment.
- Normalize scheme and host to `https://docs.gethealthie.com`.
- Treat trailing slash and no trailing slash as the same slug.
- Treat `/path/index` and `/path/` as the same slug.
- Preserve path segment casing, but reject `..` and empty unsafe segments.
- Canonical source URL format: `https://docs.gethealthie.com/<path-without-trailing-slash>`.

Discovery:

- Fetch HTML for seeds and crawled source URLs.
- Parse links with BeautifulSoup.
- Add matching internal links to a queue.
- Record every accepted URL in `discovered_urls.jsonl`.
- For every discovered relevant slug, attempt Markdown at `<canonical_slug>/index.md`.
- Parse Markdown front matter for `title`, `description`, and `source_url` when present.
- Also parse downloaded Markdown links for additional internal `/guides/` and `/reference/` URLs, but HTML navigation remains the primary source.
- When a guide links to unversioned `/reference`, either ignore it or normalize it to `/reference/<selected_reference_version>`. Do not follow the live redirect to an older version.
- When a guide or reference page links to a non-selected reference version, ignore that link for crawling and downloading.

Reference version detection:

- The selected reference version defaults to `2026-01-01`.
- Parse `guides/api-concepts/versioning/index.md`.
- Confirm that the selected version appears as a published version candidate under `## Version History (Breaking Changes)` or is explicitly passed with `--reference-version`.
- Validate only the selected version with `GET https://docs.gethealthie.com/reference/<selected_reference_version>/index.md`.
- Only enqueue `/reference/<selected_reference_version>/` when validation returns HTTP `200` and Markdown-like content.
- If the selected version does not validate, fail the crawl with a clear fatal error.
- Do not validate and enqueue every historical candidate. This repo is not a multi-version reference archive.

Markdown download:

- For canonical slug `https://docs.gethealthie.com/guides/intro`, try `https://docs.gethealthie.com/guides/intro/index.md`.
- Accept response as Markdown when:
  - HTTP status is `200`; and
  - content type contains `markdown` or body looks like Markdown/front matter; and
  - content is not HTML.
- Save using the local path mapping above.
- Compute `sha256` and byte size.

Redirect handling:

- Allow redirects for HTML and Markdown.
- Record `final_source_url` or `final_markdown_url` when different.
- If a redirect lands outside `docs.gethealthie.com`, do not crawl it.
- Do not fetch unversioned `/reference/` in latest-only mode.
- If any discovered URL redirects to a non-selected reference version, ignore it and do not save HTML fallback.

404 and grouping handling:

- Some grouping URLs may not have Markdown, for example `/guides/index.md`.
- If Markdown is 404 but HTML is 200 and internal links were extracted, continue crawling.
- Record this in `failed_urls.jsonl` with `error_type: "markdown_not_available"` and `fallback_used: "html_links_only"` or `fallback_used: "html_saved"`.
- When `--save-html-fallback` is enabled and the HTML page appears contentful, save sanitized HTML under `healthie_docs/raw_html_fallback/`.
- Do not save HTML fallback for unversioned `/reference` or for non-selected reference versions.

Politeness and robustness:

- Use a clear user agent, for example `healthie-documentation-mirror/1.0`.
- Use `--delay-seconds` between requests.
- Retry 429 and 5xx up to 2 times with simple backoff.
- Honor `Retry-After` when present.
- Do not run concurrent fetching in v1 unless explicitly added later.

## Manifest Schemas

All JSONL manifests must contain one valid JSON object per line. They must be parseable with Python `json.loads`.

### `healthie_docs/manifest/discovered_urls.jsonl`

Fields:

```json
{
  "url": "https://docs.gethealthie.com/guides/intro/",
  "normalized_url": "https://docs.gethealthie.com/guides/intro",
  "path": "/guides/intro",
  "section": "guides",
  "reference_version": null,
  "source_type": "seed|html_link|markdown_link|version_candidate|redirect",
  "discovered_from": null,
  "anchor_text": null,
  "depth": 0,
  "first_seen_at": "2026-06-27T12:00:00Z"
}
```

### `healthie_docs/manifest/downloaded_pages.jsonl`

Fields:

```json
{
  "source_url": "https://docs.gethealthie.com/guides/api-concepts/authentication",
  "final_source_url": "https://docs.gethealthie.com/guides/api-concepts/authentication",
  "markdown_url": "https://docs.gethealthie.com/guides/api-concepts/authentication/index.md",
  "final_markdown_url": "https://docs.gethealthie.com/guides/api-concepts/authentication/index.md",
  "local_path": "healthie_docs/raw/guides/api-concepts/authentication/index.md",
  "http_status": 200,
  "content_type": "text/markdown; charset=utf-8",
  "title": "Authentication | Healthie API Docs",
  "description": null,
  "section": "guides",
  "reference_version": null,
  "slug": "/guides/api-concepts/authentication",
  "sha256": "...",
  "bytes": 12345,
  "skipped_existing": false,
  "fetched_at": "2026-06-27T12:00:00Z"
}
```

### `healthie_docs/manifest/failed_urls.jsonl`

Fields:

```json
{
  "source_url": "https://docs.gethealthie.com/guides/billing/episodes-of-care",
  "final_source_url": null,
  "markdown_url": "https://docs.gethealthie.com/guides/billing/episodes-of-care/index.md",
  "http_status": 404,
  "content_type": "text/plain;charset=UTF-8",
  "error_type": "markdown_not_available",
  "error": "Markdown page was not available at index.md",
  "discovered_from": "https://docs.gethealthie.com/guides/patient-encounters-episodes-of-care/patient-encounters",
  "section": "guides",
  "reference_version": null,
  "fallback_used": null,
  "retryable": false,
  "failed_at": "2026-06-27T12:00:00Z"
}
```

Do not log historical reference versions as failures merely because they are not selected. Non-selected reference versions are out of scope and should be ignored.

### `healthie_docs/manifest/crawl_summary.json`

Fields:

```json
{
  "started_at": "2026-06-27T12:00:00Z",
  "finished_at": "2026-06-27T12:10:00Z",
  "duration_seconds": 600,
  "base_domain": "docs.gethealthie.com",
  "mode": "all",
  "refresh": false,
  "seed_urls": [],
  "selected_reference_version": "2026-01-01",
  "validated_reference_versions": ["2026-01-01"],
  "counts": {
    "discovered_urls": 0,
    "html_pages_visited": 0,
    "downloaded_pages": 0,
    "skipped_existing": 0,
    "failed_urls": 0,
    "html_fallback_pages": 0
  },
  "http_status_counts": {},
  "sections": {
    "guides": 0,
    "reference": 0
  },
  "output_dir": "healthie_docs",
  "script_version": "v1"
}
```

## Local Indexes

Generate `healthie_docs/indexes/sitemap.md`:

- Title and generation timestamp.
- "Guides" section sorted by slug.
- "Reference" section for the selected version only.
- Each entry links to the local Markdown file using a relative path.
- Include source URL beside each entry.
- Include a short "How to search" section with `rg`.

Generate `healthie_docs/indexes/sitemap.json`:

```json
{
  "generated_at": "2026-06-27T12:00:00Z",
  "pages": [
    {
      "title": "Authentication | Healthie API Docs",
      "section": "guides",
      "reference_version": null,
      "slug": "/guides/api-concepts/authentication",
      "source_url": "https://docs.gethealthie.com/guides/api-concepts/authentication",
      "markdown_url": "https://docs.gethealthie.com/guides/api-concepts/authentication/index.md",
      "local_path": "healthie_docs/raw/guides/api-concepts/authentication/index.md"
    }
  ]
}
```

## README Requirements

Update or create `README.md` so it explains:

- This repo is a local public documentation mirror for Healthie research in EPI10 Salud.
- The mirror contains public docs only.
- The mirror is latest-reference-only.
- The selected reference version is `2026-01-01` by default as of 2026-06-27.
- No Healthie credentials are required.
- How to install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- How to run:

```bash
python scripts/mirror_healthie_docs.py --mode all
python scripts/mirror_healthie_docs.py --mode crawl --refresh
python scripts/mirror_healthie_docs.py --mode index
python scripts/mirror_healthie_docs.py --mode all --reference-version 2026-01-01
```

- Where guides live: `healthie_docs/raw/guides/`
- Where reference docs live: `healthie_docs/raw/reference/2026-01-01/`
- Where manifests live: `healthie_docs/manifest/`
- Where indexes live: `healthie_docs/indexes/`
- How Codex should use it for research:

```bash
rg "AuthorizationSource" healthie_docs/raw
rg "Healthie-GraphQL-API-Version" healthie_docs/raw
rg "webhook" healthie_docs/raw/guides
```

- Explicitly state that EPI10 functional research and Healthie integration work are later phases.

## Acceptance Criteria

The executor must verify all of these:

- `scripts/mirror_healthie_docs.py --help` works.
- `requirements.txt` exists with required Python dependencies.
- `python scripts/mirror_healthie_docs.py --mode all` completes without fatal error.
- Running without `--reference-version` mirrors only the default selected reference version: `2026-01-01`.
- `--reference-version` is a single-value override, not a repeatable multi-version filter.
- URLs under `/guides/` are discovered from HTML navigation.
- URLs under `/reference/2026-01-01/` are discovered from HTML navigation.
- The selected reference version is validated before crawling.
- Unversioned `/reference` is not downloaded, not saved as HTML fallback, and not allowed to redirect the mirror to `2024-10-20`.
- Non-selected reference versions are ignored for crawling, downloading, manifests, and indexes.
- Markdown pages are downloaded via `<slug>/index.md`.
- Sample guide pages exist locally:
  - `healthie_docs/raw/guides/intro/index.md`
  - `healthie_docs/raw/guides/api-concepts/authentication/index.md`
- The selected validated reference version contains local Markdown pages.
- This sample reference page exists:
  - `healthie_docs/raw/reference/2026-01-01/enums/action/index.md`
- `healthie_docs/raw/reference/` contains only `2026-01-01`.
- Local paths preserve slug structure.
- `discovered_urls.jsonl`, `downloaded_pages.jsonl`, and `failed_urls.jsonl` exist.
- Every JSONL line parses as valid JSON.
- `crawl_summary.json` exists and contains counts.
- `crawl_summary.json` contains `"selected_reference_version": "2026-01-01"`.
- `crawl_summary.json` contains `"validated_reference_versions": ["2026-01-01"]`.
- `sitemap.md` and `sitemap.json` exist.
- `sitemap.md`, `sitemap.json`, and `downloaded_pages.jsonl` do not include `/reference/2024-` or `/reference/2025-` URLs.
- Re-running without `--refresh` does not duplicate manifest rows or redownload existing files unnecessarily.
- Re-running with `--refresh` refreshes existing files.
- 404s for in-scope pages are recorded in `failed_urls.jsonl`.
- Root `README.md` documents setup, commands, structure, and research usage.
- No credentials, API keys, private endpoints, or EPI10 data are used.
- No functional EPI10 research is performed.

Suggested validation commands:

```bash
python -m py_compile scripts/mirror_healthie_docs.py
python scripts/mirror_healthie_docs.py --help
python scripts/mirror_healthie_docs.py --mode all
python scripts/mirror_healthie_docs.py --mode index
python - <<'PY'
import json
from pathlib import Path
for path in [
    "healthie_docs/manifest/discovered_urls.jsonl",
    "healthie_docs/manifest/downloaded_pages.jsonl",
    "healthie_docs/manifest/failed_urls.jsonl",
]:
    p = Path(path)
    assert p.exists(), path
    with p.open() as f:
        for i, line in enumerate(f, 1):
            if line.strip():
                json.loads(line)
print("JSONL manifests parse")
PY
python - <<'PY'
import json
from pathlib import Path
summary = json.loads(Path("healthie_docs/manifest/crawl_summary.json").read_text())
assert summary["selected_reference_version"] == "2026-01-01"
assert summary["validated_reference_versions"] == ["2026-01-01"]
versions = sorted(p.name for p in Path("healthie_docs/raw/reference").iterdir() if p.is_dir())
assert versions == ["2026-01-01"], versions
print("latest-only reference validated")
PY
test -f healthie_docs/raw/guides/intro/index.md
test -f healthie_docs/raw/guides/api-concepts/authentication/index.md
test -f healthie_docs/raw/reference/2026-01-01/enums/action/index.md
test -f healthie_docs/indexes/sitemap.md
test -f healthie_docs/indexes/sitemap.json
! rg '/reference/(2024|2025)-[0-9]{2}-[0-9]{2}' healthie_docs/manifest/downloaded_pages.jsonl healthie_docs/indexes healthie_docs/raw/reference
test ! -f healthie_docs/raw_html_fallback/reference/index.html
```

## Risks And Defaults

- Healthie documentation navigation may change; crawler must rely on discovered HTML links, not hardcoded page lists.
- Healthie versioning docs may mention dates that are not available under `/reference/<date>/`; validate only the selected live version.
- If Healthie publishes a newer live reference version, update `--reference-version`, README, and this spec in a small maintenance change before research uses the new version.
- Some grouping pages may not expose Markdown; log them and continue.
- `sitemap.xml` and `robots.txt` were not useful during planning; do not depend on them.
- Use static HTTP crawling first. Do not use browser automation unless static crawling demonstrably misses public navigation.

## Executor prompt

```text
/goal Ajusta la implementacion existente para cumplir la spec `specs/healthie_docs_mirror_spec_v1.md` en modo latest-reference-only. Lee primero `AGENTS.md`, `01_harness/RULES.md`, `01_harness/STACK.md`, `01_harness/TASKFLOW.md` y la spec completa. Cambia `scripts/mirror_healthie_docs.py` para que `python scripts/mirror_healthie_docs.py --mode all` descargue guias publicas completas y solo la reference seleccionada `2026-01-01` por defecto. `--reference-version` debe ser un override unico, no un filtro multi-version repetible. Elimina seeds antiguos (`2024-06-01`, `2024-10-20`) y no uses `/reference/` sin version como seed ni como HTML fallback, porque redirige a `2024-10-20`. Filtra o ignora cualquier link a versiones no seleccionadas. Limpia artefactos stale para que `healthie_docs/raw/reference/` solo contenga `2026-01-01`, y para que manifests e indices no incluyan `/reference/2024-` ni `/reference/2025-`. Actualiza README y la nota de entrega si hace falta, ejecuta un mirror latest-only completo, valida todos los criterios de aceptacion de la spec y reporta resultados. No hagas research funcional de EPI10 todavia; no uses credenciales, API keys, datos reales, endpoints autenticados ni agent-browser como primera opcion.
```
