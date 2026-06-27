---
title: FoodNutrient | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/foodnutrient/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/foodnutrient/index.md
---

A food nutrient item object

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of the nutrient

[`fdc_import` ](#field-fdc-import)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the nutrient is imported from the FDC database

[`food_id` ](#field-food-id)· [`String` ](/reference/2026-01-01/scalars/string)· The unique identifier of the food

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the nutrient

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the nutrient

[`nutrient_unit` ](#field-nutrient-unit)· [`String` ](/reference/2026-01-01/scalars/string)· The unit of the nutrient

[`nutrient_value` ](#field-nutrient-value)· [`Float` ](/reference/2026-01-01/scalars/float)· The value of the nutrient

## Used By

[`Food.nutrients`](/reference/2026-01-01/objects/food)

[`ServingSize.macro_micro_nutrients`](/reference/2026-01-01/objects/servingsize)

[`ServingSize.macro_nutrients`](/reference/2026-01-01/objects/servingsize)

[`ServingSize.nutrients`](/reference/2026-01-01/objects/servingsize)

## Definition

```
"""
A food nutrient item object
"""
type FoodNutrient {
  """
  The category of the nutrient
  """
  category: String


  """
  Whether the nutrient is imported from the FDC database
  """
  fdc_import: Boolean!


  """
  The unique identifier of the food
  """
  food_id: String


  """
  The unique identifier of the nutrient
  """
  id: ID!


  """
  The name of the nutrient
  """
  name: String


  """
  The unit of the nutrient
  """
  nutrient_unit: String


  """
  The value of the nutrient
  """
  nutrient_value: Float
}
```
