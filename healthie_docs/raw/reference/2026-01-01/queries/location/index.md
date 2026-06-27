---
title: location | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/location/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/location/index.md
---

fetch a location by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Location`](/reference/2026-01-01/objects/location)

## Example

```
query location($id: ID) {
  location(id: $id) {
    city
    country
    id
    line1
    line2
    name
    npi
    other_id
    other_id_qual
    place_of_service
    place_of_service_id
    state
    to_oneline
    user
    user_id
    zip
  }
}
```
