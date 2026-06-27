---
title: noteViewedStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/noteviewedstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/noteviewedstatus/index.md
---

get the viewed status of a note

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Boolean`](/reference/2026-01-01/scalars/boolean)

## Example

```
query noteViewedStatus($id: ID) {
  noteViewedStatus(id: $id)
}
```
