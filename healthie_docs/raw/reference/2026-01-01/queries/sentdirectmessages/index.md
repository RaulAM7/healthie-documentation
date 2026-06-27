---
title: sentDirectMessages | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sentdirectmessages/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sentdirectmessages/index.md
---

Fetch paginated Sent Direct Messages collection

## Arguments

[`offset` ](#argument-offset)· [`Int`](/reference/2026-01-01/scalars/int)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`SentDirectMessageOrderKeys`](/reference/2026-01-01/enums/sentdirectmessageorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`SentDirectMessagePaginationConnection`](/reference/2026-01-01/objects/sentdirectmessagepaginationconnection)

## Example

```
query sentDirectMessages(
  $offset: Int
  $keywords: String
  $order_by: SentDirectMessageOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  sentDirectMessages(
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
