---
title: insuranceAuthorization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/insuranceauthorization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/insuranceauthorization/index.md
---

Insurance Authorization belonging to a client

## Arguments

[`client_id` ](#argument-client-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Client to get insurance authorization for

[`id` ](#argument-id)· [`ID` ](/reference/2026-01-01/scalars/id)· id of insurance authorization

## Returns

[`InsuranceAuthorizationType`](/reference/2026-01-01/objects/insuranceauthorizationtype)

## Example

```
query insuranceAuthorization($client_id: ID, $id: ID) {
  insuranceAuthorization(client_id: $client_id, id: $id) {
    authorization_number
    chart_info
    end_on
    id
    start_on
    unit_type
    units_authorized
    units_left
    units_limit_per_visit
    units_used
    updated_at
    user_id
    visits_authorized
    visits_left
    visits_used
  }
}
```
