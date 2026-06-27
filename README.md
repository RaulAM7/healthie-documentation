# Healthie Public Docs Mirror

Local mirror of the public Healthie documentation for EPI10 Salud technical research.

This repository contains public documentation only:

- The mirror is latest-reference-only.
- No Healthie credentials are required.
- No authenticated endpoints are used.
- No customer, patient, provider, or EPI10 production data is used.
- Functional EPI10 research and Healthie integration work are later phases.
- The default selected reference version is `2026-01-01` as of 2026-06-27.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python scripts/mirror_healthie_docs.py --mode all
python scripts/mirror_healthie_docs.py --mode crawl --refresh
python scripts/mirror_healthie_docs.py --mode index
python scripts/mirror_healthie_docs.py --mode all --reference-version 2026-01-01
```

## Structure

- Guides: `healthie_docs/raw/guides/`
- Latest reference docs: `healthie_docs/raw/reference/2026-01-01/`
- Manifests: `healthie_docs/manifest/`
- Indexes: `healthie_docs/indexes/`
- HTML fallback pages, when needed: `healthie_docs/raw_html_fallback/`

## Research usage

```bash
rg "AuthorizationSource" healthie_docs/raw
rg "Healthie-GraphQL-API-Version" healthie_docs/raw
rg "webhook" healthie_docs/raw/guides
```

## Notes

- The crawler discovers public documentation from static HTML navigation.
- Reference versions are validated before versioned reference trees are mirrored.
- The current repo state keeps only the latest validated reference tree locally.
- `--reference-version` is a single-value override for the selected live reference tree.
- Markdown is downloaded from `<slug>/index.md` when available.
- Pages without Markdown are logged in `healthie_docs/manifest/failed_urls.jsonl`.
