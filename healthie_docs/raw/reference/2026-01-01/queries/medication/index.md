---
title: medication | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/medication/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/medication/index.md
---

Fetch a medication by ID

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`MedicationType`](/reference/2026-01-01/objects/medicationtype)

## Example

```
query medication($id: ID) {
  medication(id: $id) {
    active
    code
    comment
    created_at
    directions
    dosage
    end_date
    frequency
    id
    mirrored
    name
    normalized_status
    requires_consolidation
    route
    start_date
    updated_at
    user_id
  }
}
```
