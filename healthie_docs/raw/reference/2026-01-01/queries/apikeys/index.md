---
title: apiKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/apikeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/apikeys/index.md
---

Fetch paginated API Keys collection

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`ApiKeyOrderKeys`](/reference/2026-01-01/enums/apikeyorderkeys)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ApiKeyPaginationConnection`](/reference/2026-01-01/objects/apikeypaginationconnection)

## Example

```
query apiKeys(
  $keywords: String
  $order_by: ApiKeyOrderKeys
  $sort_by: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  apiKeys(
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
