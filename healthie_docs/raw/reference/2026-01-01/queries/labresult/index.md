---
title: labResult | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/labresult/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/labresult/index.md
---

Fetch a laboratory result by ID

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the lab result

## Returns

[`LabResult`](/reference/2026-01-01/objects/labresult)

## Example

```
query labResult($id: ID!) {
  labResult(id: $id) {
    created_at
    document
    id
    interpretation
    lab_observation_requests
    lab_order_id
    ordering_physician
    patient
    result_type
    status_flag
  }
}
```
