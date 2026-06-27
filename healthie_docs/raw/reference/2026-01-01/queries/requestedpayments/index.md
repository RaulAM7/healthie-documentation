---
title: requestedPayments | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/requestedpayments/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/requestedpayments/index.md
---

Fetch paginated Requested Payments collection

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`only_unpaid` ](#argument-only-unpaid)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· (DEPRECATED) Use status\_filter instead

[`preview` ](#argument-preview)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`sender_id` ](#argument-sender-id)· [`ID` ](/reference/2026-01-01/scalars/id)· will return all requested payments with this ID as the sender or recipient

[`status_filter` ](#argument-status-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be paid, partial or unpaid

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`RequestedPaymentOrderKeys`](/reference/2026-01-01/enums/requestedpaymentorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`RequestedPaymentPaginationConnection`](/reference/2026-01-01/objects/requestedpaymentpaginationconnection)

## Example

```
query requestedPayments(
  $keywords: String
  $only_unpaid: Boolean
  $preview: Boolean
  $sender_id: ID
  $status_filter: String
  $sort_by: String
  $order_by: RequestedPaymentOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  requestedPayments(
    keywords: $keywords
    only_unpaid: $only_unpaid
    preview: $preview
    sender_id: $sender_id
    status_filter: $status_filter
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
