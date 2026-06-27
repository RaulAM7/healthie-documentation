---
title: mealSearch | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/mealsearch/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/mealsearch/index.md
---

Fetch user meals

## Arguments

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`user_id` ](#argument-user-id)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`MealPaginationConnection`](/reference/2026-01-01/objects/mealpaginationconnection)

## Example

```
query mealSearch(
  $keywords: String
  $user_id: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  mealSearch(
    keywords: $keywords
    user_id: $user_id
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
