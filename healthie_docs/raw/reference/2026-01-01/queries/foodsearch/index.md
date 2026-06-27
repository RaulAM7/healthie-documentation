---
title: foodSearch | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/foodsearch/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/foodsearch/index.md
---

Fetch food items

## Arguments

[`exclude_recent` ](#argument-exclude-recent)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`food_type` ](#argument-food-type)· [`String`](/reference/2026-01-01/scalars/string)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`upc` ](#argument-upc)· [`String`](/reference/2026-01-01/scalars/string)

[`user_id` ](#argument-user-id)· [`String`](/reference/2026-01-01/scalars/string)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`FoodPaginationConnection`](/reference/2026-01-01/objects/foodpaginationconnection)

## Example

```
query foodSearch(
  $exclude_recent: Boolean
  $food_type: String
  $keywords: String
  $upc: String
  $user_id: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  foodSearch(
    exclude_recent: $exclude_recent
    food_type: $food_type
    keywords: $keywords
    upc: $upc
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
