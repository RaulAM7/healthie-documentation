---
title: icdCodes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/icdcodes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/icdcodes/index.md
---

All ICD Codes

## Arguments

[`is_billable` ](#argument-is-billable)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, will only return billable ICD codes. When false, will only return non-billable ICD codes. When not included, will return all ICD codes.

[`is_favorited` ](#argument-is-favorited)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The favorited status of the ICD Code

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`only_valid` ](#argument-only-valid)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· when true, only codes considered to be currently valid will be returned. When false, does nothing

[`order_by` ](#argument-order-by)· [`IcdCodeOrderKeys`](/reference/2026-01-01/enums/icdcodeorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`IcdCodePaginationConnection`](/reference/2026-01-01/objects/icdcodepaginationconnection)

## Example

```
query icdCodes(
  $is_billable: Boolean
  $is_favorited: Boolean
  $keywords: String
  $only_valid: Boolean
  $order_by: IcdCodeOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  icdCodes(
    is_billable: $is_billable
    is_favorited: $is_favorited
    keywords: $keywords
    only_valid: $only_valid
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
