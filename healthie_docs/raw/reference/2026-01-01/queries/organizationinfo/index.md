---
title: organizationInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/organizationinfo/index.md
---

Fetch organization info by id

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`OrganizationInfo`](/reference/2026-01-01/objects/organizationinfo)

## Example

```
query organizationInfo($id: ID) {
  organizationInfo(id: $id) {
    created_at
    external_id
    id
    id_number_type
    location
    name
    npi
    organization
    other_id
    other_id_qual
    phone_number
    primary
    tax_id
    tax_id_type
  }
}
```
