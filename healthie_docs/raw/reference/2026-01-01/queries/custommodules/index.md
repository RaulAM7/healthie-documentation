---
title: customModules | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/custommodules/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/custommodules/index.md
---

Fetch paginated copied fields (is\_custom custom modules) for the current user

## Arguments

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Filter copied fields by label

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CustomModulePaginationConnection`](/reference/2026-01-01/objects/custommodulepaginationconnection)

## Example

```
query customModules(
  $keywords: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  customModules(
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
