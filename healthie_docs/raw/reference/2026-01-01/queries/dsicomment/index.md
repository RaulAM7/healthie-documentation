---
title: dsiComment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/dsicomment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/dsicomment/index.md
---

Fetch DSI comment for given intervention\_type

## Arguments

[`intervention_type` ](#argument-intervention-type)· [`InterventionType`](/reference/2026-01-01/enums/interventiontype)

## Returns

[`DsiComment`](/reference/2026-01-01/objects/dsicomment)

## Example

```
query dsiComment($intervention_type: InterventionType) {
  dsiComment(intervention_type: $intervention_type) {
    content
    id
    intervention_type
    organization_id
  }
}
```
