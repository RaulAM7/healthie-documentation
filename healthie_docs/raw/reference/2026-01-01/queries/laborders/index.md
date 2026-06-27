---
title: labOrders | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/laborders/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/laborders/index.md
---

Fetch Lab Orders collection

## Arguments

[`client_filter` ](#argument-client-filter)· [`String`](/reference/2026-01-01/scalars/string)

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`lab_filter` ](#argument-lab-filter)· [`String`](/reference/2026-01-01/scalars/string)

[`orderer_filter` ](#argument-orderer-filter)· [`String`](/reference/2026-01-01/scalars/string)

[`provider_filter` ](#argument-provider-filter)· [`String`](/reference/2026-01-01/scalars/string)

[`reviewing_provider_filter` ](#argument-reviewing-provider-filter)· [`String`](/reference/2026-01-01/scalars/string)

[`recent_orders` ](#argument-recent-orders)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`LabOrderOrderKeys`](/reference/2026-01-01/enums/laborderorderkeys)

[`status_filter` ](#argument-status-filter)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`LabOrderPaginationConnection`](/reference/2026-01-01/objects/laborderpaginationconnection)

## Example

```
query labOrders(
  $client_filter: String
  $client_id: ID
  $keywords: String
  $lab_filter: String
  $orderer_filter: String
  $provider_filter: String
  $reviewing_provider_filter: String
  $recent_orders: Boolean
  $sort_by: String
  $order_by: LabOrderOrderKeys
  $status_filter: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  labOrders(
    client_filter: $client_filter
    client_id: $client_id
    keywords: $keywords
    lab_filter: $lab_filter
    orderer_filter: $orderer_filter
    provider_filter: $provider_filter
    reviewing_provider_filter: $reviewing_provider_filter
    recent_orders: $recent_orders
    sort_by: $sort_by
    order_by: $order_by
    status_filter: $status_filter
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
