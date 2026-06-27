---
title: pharmacy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/pharmacy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/pharmacy/index.md
---

Fetch a pharmacy given dosespot pharmacy id

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · id assigned by dosespot

## Returns

[`Pharmacy`](/reference/2026-01-01/objects/pharmacy)

## Example

```
query pharmacy($id: ID!) {
  pharmacy(id: $id) {
    city
    fax_number
    id
    latitude
    line1
    line2
    longitude
    name
    ncpdpid
    phone_number
    service_level
    specialties
    state
    zip
  }
}
```
