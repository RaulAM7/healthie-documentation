---
title: sentFaxes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/sentfaxes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/sentfaxes/index.md
---

Fetch paginated Sent Faxes collection

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`SentFaxOrderKeys`](/reference/2026-01-01/enums/sentfaxorderkeys)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`SentFaxPaginationConnection`](/reference/2026-01-01/objects/sentfaxpaginationconnection)

## Example

```
query sentFaxes(
  $keywords: String
  $order_by: SentFaxOrderKeys
  $sort_by: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  sentFaxes(
    keywords: $keywords
    order_by: $order_by
    sort_by: $sort_by
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
