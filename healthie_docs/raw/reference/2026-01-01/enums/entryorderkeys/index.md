---
title: EntryOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/entryorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/entryorderkeys/index.md
---

Entry sorting enum

## Used By

[`Query.entries`](/reference/2026-01-01/queries/entries)

## Definition

```
"""
Entry sorting enum
"""
enum EntryOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
  METRIC_STAT_ASC
  METRIC_STAT_DESC
  THIRD_PARTY_SOURCE_ASC
  THIRD_PARTY_SOURCE_DESC
  UNSORTED
}
```
