---
title: cptCodes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/cptcodes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/cptcodes/index.md
---

All CPT Codes

## Arguments

[`for_superbill` ](#argument-for-superbill)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`is_favorited` ](#argument-is-favorited)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CptCodePaginationConnection`](/reference/2026-01-01/objects/cptcodepaginationconnection)

## Example

```
query cptCodes(
  $for_superbill: Boolean
  $is_favorited: Boolean
  $keywords: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  cptCodes(
    for_superbill: $for_superbill
    is_favorited: $is_favorited
    keywords: $keywords
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
