---
title: receivedDirectMessages | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/receiveddirectmessages/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/receiveddirectmessages/index.md
---

Fetch paginated Received Direct Messages collection

## Arguments

[`offset` ](#argument-offset)· [`Int`](/reference/2026-01-01/scalars/int)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`ReceivedDirectMessageOrderKeys`](/reference/2026-01-01/enums/receiveddirectmessageorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ReceivedDirectMessagePaginationConnection`](/reference/2026-01-01/objects/receiveddirectmessagepaginationconnection)

## Example

```
query receivedDirectMessages(
  $offset: Int
  $keywords: String
  $order_by: ReceivedDirectMessageOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  receivedDirectMessages(
    offset: $offset
    keywords: $keywords
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
