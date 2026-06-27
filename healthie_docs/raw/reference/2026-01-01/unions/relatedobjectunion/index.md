---
title: RelatedObjectUnion | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/unions/relatedobjectunion/index
  md: https://docs.gethealthie.com/reference/2026-01-01/unions/relatedobjectunion/index.md
---

The related record associated with a form answer group audit event, which varies depending on the action that occurred.

## Possible types

[`ChartingNoteAddendumType`](#field-chartingnoteaddendumtype)

[`FormAnswerGroupSigning`](#field-formanswergroupsigning)

## Used By

[`FormAnswerGroupAuditEvent.related_object`](/reference/2026-01-01/objects/formanswergroupauditevent)

## Definition

```
"""
The related record associated with a form answer group audit event, which varies depending on the action that occurred.
"""
union RelatedObjectUnion = ChartingNoteAddendumType | FormAnswerGroupSigning
```
