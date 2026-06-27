---
title: chargeBacks | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/chargebacks/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/chargebacks/index.md
---

fetch all charge backs for a user or organization

## Arguments

[`show_all_for_org` ](#argument-show-all-for-org)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If user has access to all billing for their organization, this will return all chargebacks for the organization

[`order_by` ](#argument-order-by)· [`ChargeBackOrderKeys`](/reference/2026-01-01/enums/chargebackorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ChargeBackPaginationConnection`](/reference/2026-01-01/objects/chargebackpaginationconnection)

## Example

```
query chargeBacks(
  $show_all_for_org: Boolean
  $order_by: ChargeBackOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  chargeBacks(
    show_all_for_org: $show_all_for_org
    order_by: $order_by
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
