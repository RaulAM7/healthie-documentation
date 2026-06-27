---
title: chartingNoteAddendum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/chartingnoteaddendum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/chartingnoteaddendum/index.md
---

Fetch a charting note addendum by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`ChartingNoteAddendumType`](/reference/2026-01-01/objects/chartingnoteaddendumtype)

## Example

```
query chartingNoteAddendum($id: ID) {
  chartingNoteAddendum(id: $id) {
    content
    created_at
    form_answer_group
    id
    user
  }
}
```
