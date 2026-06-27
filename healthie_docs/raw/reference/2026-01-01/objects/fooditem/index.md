---
title: FoodItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/fooditem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/fooditem/index.md
---

A food item to be served

## Fields

[`food` ](#field-food)· [`Food` ](/reference/2026-01-01/objects/food)· The food to be served

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the food item

[`modifier` ](#field-modifier)· [`Float` ](/reference/2026-01-01/scalars/float)· The modifier for the serving size

[`serving_size` ](#field-serving-size)· [`ServingSize` ](/reference/2026-01-01/objects/servingsize)· The serving size

## Used By

[`Meal.food_items`](/reference/2026-01-01/objects/meal)

## Definition

```
"""
A food item to be served
"""
type FoodItem {
  """
  The food to be served
  """
  food: Food


  """
  The unique identifier of the food item
  """
  id: ID!


  """
  The modifier for the serving size
  """
  modifier: Float


  """
  The serving size
  """
  serving_size: ServingSize
}
```
