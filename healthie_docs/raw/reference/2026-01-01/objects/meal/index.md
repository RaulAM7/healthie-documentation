---
title: Meal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/meal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/meal/index.md
---

A meal that a user has created

## Fields

[`food_items` ](#field-food-items)· [`[FoodItem!]` ](/reference/2026-01-01/objects/fooditem)· The food items that are part of the meal

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the meal

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the meal

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The user that owns the meal

## Used By

[`Entry.meals`](/reference/2026-01-01/objects/entry)

[`MealEdge.node`](/reference/2026-01-01/objects/mealedge)

[`MealPaginationConnection.nodes`](/reference/2026-01-01/objects/mealpaginationconnection)

[`createMealPayload.meal`](/reference/2026-01-01/objects/createmealpayload)

[`deleteMealPayload.meal`](/reference/2026-01-01/objects/deletemealpayload)

[`updateMealPayload.meal`](/reference/2026-01-01/objects/updatemealpayload)

## Definition

```
"""
A meal that a user has created
"""
type Meal {
  """
  The food items that are part of the meal
  """
  food_items: [FoodItem!]


  """
  The unique identifier of the meal
  """
  id: ID!


  """
  The name of the meal
  """
  name: String


  """
  The user that owns the meal
  """
  user_id: String
}
```
