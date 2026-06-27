---
title: initializedOfferingIncludes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/initializedofferingincludes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/initializedofferingincludes/index.md
---

appointment types related to offering

## Arguments

[`offering_id` ](#argument-offering-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`[OfferingInclude!]`](/reference/2026-01-01/objects/offeringinclude)

## Example

```
query initializedOfferingIncludes($offering_id: ID) {
  initializedOfferingIncludes(offering_id: $offering_id) {
    appointment_type
    appointment_type_id
    created_at
    expires_in
    form_id
    id
    is_repeating
    offering_id
    quantity
    required_appointment_type
    updated_at
  }
}
```
