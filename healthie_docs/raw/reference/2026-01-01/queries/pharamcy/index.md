---
title: pharamcy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/pharamcy/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/pharamcy/index.md
---

deprecated Use \`pharmacy\` instead

Fetch a pharmacy given dosespot pharmacy id

## Arguments

[`id` ](#argument-id)· [`String` ](/reference/2026-01-01/scalars/string)· id assigned by dosespot

## Returns

[`Pharmacy`](/reference/2026-01-01/objects/pharmacy)

## Example

```
query pharamcy($id: String) {
  pharamcy(id: $id) {
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
