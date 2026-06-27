---
title: ChartNoteStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/chartnotestatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/chartnotestatus/index.md
---

Chart note statuses

## Used By

[`FormAnswerGroup.chart_note_status`](/reference/2026-01-01/objects/formanswergroup)

[`Query.chartNotes`](/reference/2026-01-01/queries/chartnotes)

## Definition

```
"""
Chart note statuses
"""
enum ChartNoteStatus {
  CREATED
  SIGNED
  CO_SIGNED
  LOCKED
  CO_SIGNED_AND_LOCKED
  SIGNED_AND_LOCKED
}
```
