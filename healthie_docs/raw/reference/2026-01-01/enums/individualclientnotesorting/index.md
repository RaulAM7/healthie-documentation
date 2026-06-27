---
title: IndividualClientNoteSorting | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/individualclientnotesorting/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/individualclientnotesorting/index.md
---

Individual client note sorting enum

## Used By

[`FormAnswerGroup.individual_client_notes`](/reference/2026-01-01/objects/formanswergroup)

## Definition

```
"""
Individual client note sorting enum
"""
enum IndividualClientNoteSorting {
  ATTENDED_DESC
    @deprecated(
      reason: "Use `IndividualClientNoteOrderKeys` and `order_by` instead"
    )
  CREATED_AT_DESC
    @deprecated(
      reason: "Use `IndividualClientNoteOrderKeys` and `order_by` instead"
    )
}
```
