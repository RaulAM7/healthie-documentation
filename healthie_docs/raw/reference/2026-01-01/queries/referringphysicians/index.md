---
title: referringPhysicians | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/referringphysicians/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/referringphysicians/index.md
---

all referring physicians based on current user

## Arguments

[`has_fax_number` ](#argument-has-fax-number)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`ReferringPhysicianOrderKeys`](/reference/2026-01-01/enums/referringphysicianorderkeys)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ReferringPhysicianPaginationConnection`](/reference/2026-01-01/objects/referringphysicianpaginationconnection)

## Example

```
query referringPhysicians(
  $has_fax_number: Boolean
  $keywords: String
  $order_by: ReferringPhysicianOrderKeys
  $sort_by: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  referringPhysicians(
    has_fax_number: $has_fax_number
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
