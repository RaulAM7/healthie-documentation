---
title: providerAcceptedInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/provideracceptedinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/provideracceptedinsuranceplan/index.md
---

Fetch a single accepted insurance plan for a provider

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the provider accepted insurance plan

## Returns

[`ProviderAcceptedInsurancePlanType`](/reference/2026-01-01/objects/provideracceptedinsuranceplantype)

## Example

```
query providerAcceptedInsurancePlan($id: ID!) {
  providerAcceptedInsurancePlan(id: $id) {
    accepted_insurance_plan
    id
    organization
    provider
  }
}
```
