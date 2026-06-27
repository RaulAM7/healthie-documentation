---
title: recentFoods | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/recentfoods/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/recentfoods/index.md
---

Fetch recent food items

## Arguments

[`food_type` ](#argument-food-type)· [`String`](/reference/2026-01-01/scalars/string)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`user_id` ](#argument-user-id)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`[Food!]`](/reference/2026-01-01/objects/food)

## Example

```
query recentFoods($food_type: String, $keywords: String, $user_id: String) {
  recentFoods(food_type: $food_type, keywords: $keywords, user_id: $user_id) {
    creator_name
    default_serving_size
    display_name
    edamam_import_id
    fdc_import
    id
    name
    nutrients
    serving_sizes
    user_id
  }
}
```
