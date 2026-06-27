---
title: receivedFaxes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/receivedfaxes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/receivedfaxes/index.md
---

Fetch paginated Received Faxes collection

## Arguments

[`active_status` ](#argument-active-status)· [`String`](/reference/2026-01-01/scalars/string)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`ReceivedFaxOrderKeys`](/reference/2026-01-01/enums/receivedfaxorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ReceivedFaxPaginationConnection`](/reference/2026-01-01/objects/receivedfaxpaginationconnection)

## Example

```
query receivedFaxes(
  $active_status: String
  $keywords: String
  $sort_by: String
  $order_by: ReceivedFaxOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  receivedFaxes(
    active_status: $active_status
    keywords: $keywords
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
