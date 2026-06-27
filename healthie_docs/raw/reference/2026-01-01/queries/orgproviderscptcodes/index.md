---
title: orgProvidersCptCodes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/orgproviderscptcodes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/orgproviderscptcodes/index.md
---

Fetch paginated org providers CPT codes collection

## Arguments

[`org_id` ](#argument-org-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ProviderCptCodeTypePaginationConnection`](/reference/2026-01-01/objects/providercptcodetypepaginationconnection)

## Example

```
query orgProvidersCptCodes(
  $org_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  orgProvidersCptCodes(
    org_id: $org_id
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
