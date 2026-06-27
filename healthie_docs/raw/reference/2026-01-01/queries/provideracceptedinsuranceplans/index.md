---
title: providerAcceptedInsurancePlans | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/provideracceptedinsuranceplans/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/provideracceptedinsuranceplans/index.md
---

Fetch paginated provider accepted insurance plans collection

## Arguments

[`provider_id` ](#argument-provider-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the provider to fetch plans for

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ProviderAcceptedInsurancePlanTypePaginationConnection!`](/reference/2026-01-01/objects/provideracceptedinsuranceplantypepaginationconnection)

## Example

```
query providerAcceptedInsurancePlans(
  $provider_id: ID!
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  providerAcceptedInsurancePlans(
    provider_id: $provider_id
    after: $after
    before: $before
    first: $first
    last: $last
  )
}
```
