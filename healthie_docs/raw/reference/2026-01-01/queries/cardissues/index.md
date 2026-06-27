---
title: cardIssues | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/cardissues/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/cardissues/index.md
---

Fetch paginated stripe customer accounts with associated errors or soon to expire credit cards

## Arguments

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`StripeCustomerDetailOrderKeys`](/reference/2026-01-01/enums/stripecustomerdetailorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`StripeCustomerDetailPaginationConnection`](/reference/2026-01-01/objects/stripecustomerdetailpaginationconnection)

## Example

```
query cardIssues(
  $sort_by: String
  $order_by: StripeCustomerDetailOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  cardIssues(
    sort_by: $sort_by
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
