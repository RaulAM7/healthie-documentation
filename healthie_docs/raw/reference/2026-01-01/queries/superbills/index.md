---
title: superBills | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/superbills/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/superbills/index.md
---

Fetch paginated super bills collection

## Arguments

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`provider_id` ](#argument-provider-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`SuperBillOrderKeys`](/reference/2026-01-01/enums/superbillorderkeys)

[`status` ](#argument-status)· [`String` ](/reference/2026-01-01/scalars/string)· status to filter superbills, default all

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`SuperBillPaginationConnection`](/reference/2026-01-01/objects/superbillpaginationconnection)

## Example

```
query superBills(
  $client_id: ID
  $keywords: String
  $provider_id: ID
  $sort_by: String
  $order_by: SuperBillOrderKeys
  $status: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  superBills(
    client_id: $client_id
    keywords: $keywords
    provider_id: $provider_id
    sort_by: $sort_by
    order_by: $order_by
    status: $status
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
