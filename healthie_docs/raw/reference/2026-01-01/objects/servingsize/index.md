---
title: ServingSize | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/servingsize/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/servingsize/index.md
---

A serving size object

## Fields

[`amount` ](#field-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· The number of servings

[`calories` ](#field-calories)· [`Float` ](/reference/2026-01-01/scalars/float)· The calories of serving size

[`fdc_import` ](#field-fdc-import)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not this serving size was imported from the USDA database

[`food_id` ](#field-food-id)· [`String` ](/reference/2026-01-01/scalars/string)· The food id of the food this serving size belongs to

[`food_portion_id` ](#field-food-portion-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the food portion this serving size belongs to

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the serving size

[`macro_micro_nutrients` ](#field-macro-micro-nutrients)· [`[FoodNutrient!]` ](/reference/2026-01-01/objects/foodnutrient)· The macro & micro nutrients of this serving size

[`macro_nutrients` ](#field-macro-nutrients)· [`[FoodNutrient!]` ](/reference/2026-01-01/objects/foodnutrient)· The macro nutrients of this serving size (Calories, Carbohydrate, Protein, Fat)

[`modifier` ](#field-modifier)· [`Float` ](/reference/2026-01-01/scalars/float)· percentage of 100g. For example if modifier is 2.5 then this serving size is 250g

[`nutrients` ](#field-nutrients)· [`[FoodNutrient!]` ](/reference/2026-01-01/objects/foodnutrient)· The nutrients of this serving size

[`unit` ](#field-unit)· [`String` ](/reference/2026-01-01/scalars/string)· The type of serving (i.e grams, scoop, spoonful)

## Used By

[`Food.default_serving_size`](/reference/2026-01-01/objects/food)

[`Food.serving_sizes`](/reference/2026-01-01/objects/food)

[`FoodItem.serving_size`](/reference/2026-01-01/objects/fooditem)

[`ServingSizeEdge.node`](/reference/2026-01-01/objects/servingsizeedge)

[`ServingSizePaginationConnection.nodes`](/reference/2026-01-01/objects/servingsizepaginationconnection)

## Definition

```
"""
A serving size object
"""
type ServingSize {
  """
  The number of servings
  """
  amount: Float


  """
  The calories of serving size
  """
  calories: Float


  """
  Whether or not this serving size was imported from the USDA database
  """
  fdc_import: Boolean!


  """
  The food id of the food this serving size belongs to
  """
  food_id: String


  """
  The id of the food portion this serving size belongs to
  """
  food_portion_id: ID


  """
  The unique identifier of the serving size
  """
  id: ID!


  """
  The macro & micro nutrients of this serving size
  """
  macro_micro_nutrients: [FoodNutrient!]


  """
  The macro nutrients of this serving size (Calories, Carbohydrate, Protein, Fat)
  """
  macro_nutrients: [FoodNutrient!]


  """
  percentage of 100g. For example if modifier is 2.5 then this serving size is 250g
  """
  modifier: Float


  """
  The nutrients of this serving size
  """
  nutrients(
    """
    If true, only returns nutrients if food is created by user ()
    """
    food_search: Boolean
  ): [FoodNutrient!]


  """
  The type of serving (i.e grams, scoop, spoonful)
  """
  unit: String
}
```
