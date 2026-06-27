# Healthie Public Docs Mirror v1

## Status
- Pass.

## Delivered
- `scripts/mirror_healthie_docs.py`
- `requirements.txt`
- `healthie_docs/` public-doc mirror structure
- `healthie_docs/manifest/` manifests
- `healthie_docs/indexes/` local indexes
- Root `README.md`

Delivered repo state on 2026-06-27:

- Guides mirrored locally: `58`
- Latest reference version mirrored locally: `2026-01-01`
- Latest reference pages mirrored locally: `2349`
- Total mirrored Markdown pages: `2407`
- Failed public Markdown URLs logged: `2`

## Validation
- `python -m py_compile scripts/mirror_healthie_docs.py`: pass
- `python scripts/mirror_healthie_docs.py --help`: pass
- `python scripts/mirror_healthie_docs.py --mode all`: pass
- `python scripts/mirror_healthie_docs.py --mode index`: pass
- repeated `--reference-version`: rejected as expected
- JSONL manifests parse with `json.loads`: pass
- Sample files exist:
  - `healthie_docs/raw/guides/intro/index.md`
  - `healthie_docs/raw/guides/api-concepts/authentication/index.md`
  - `healthie_docs/raw/reference/2026-01-01/enums/action/index.md`
  - `healthie_docs/indexes/sitemap.md`
  - `healthie_docs/indexes/sitemap.json`
- `crawl_summary.json` contains `selected_reference_version = "2026-01-01"` and `validated_reference_versions = ["2026-01-01"]`: pass
- `healthie_docs/raw/reference/` contains only `2026-01-01`: pass
- No `/reference/2024-*` or `/reference/2025-*` URLs remain in manifests, indexes, or local reference tree: pass
- Re-run without `--refresh`: pass (`skipped_existing=2407`)
- Re-run with `--refresh`: pass in smoke rerun (`max-pages=6`, `skipped_existing=0`, file mtimes updated)
- Unversioned `/reference` is not downloaded and no `raw_html_fallback/reference/index.html` is produced: pass

## Unknowns
- None for the mirrored public scope.

## Risks
- Public Healthie docs can change over time; the mirror is only as current as the last crawl run.
- Two public URLs still do not expose Markdown and are correctly logged in `healthie_docs/manifest/failed_urls.jsonl`:
  - `/guides/billing/episodes-of-care`
  - `/guides/billing/patient-encounters`
