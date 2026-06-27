---
title: Food | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/food/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/food/index.md
---

A food object

## Fields

[`creator_name` ](#field-creator-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the food creator

[`default_serving_size` ](#field-default-serving-size)· [`ServingSize` ](/reference/2026-01-01/objects/servingsize)· first serving size of the food object

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the food to display

[`edamam_import_id` ](#field-edamam-import-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the food in the Edamam database

[`fdc_import` ](#field-fdc-import)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the food was imported from the FDC database

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the food

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the food

[`nutrients` ](#field-nutrients)· [`[FoodNutrient!]` ](/reference/2026-01-01/objects/foodnutrient)· Nutrients of the food object

[`serving_sizes` ](#field-serving-sizes)· [`[ServingSize!]` ](/reference/2026-01-01/objects/servingsize)· Serving sizes of the food object

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user who created the food

## Used By

[`FoodEdge.node`](/reference/2026-01-01/objects/foodedge)

[`FoodItem.food`](/reference/2026-01-01/objects/fooditem)

[`FoodPaginationConnection.nodes`](/reference/2026-01-01/objects/foodpaginationconnection)

[`createCustomFoodPayload.customFood`](/reference/2026-01-01/objects/createcustomfoodpayload)

[`deleteCustomFoodPayload.customFood`](/reference/2026-01-01/objects/deletecustomfoodpayload)

[`updateCustomFoodPayload.customFood`](/reference/2026-01-01/objects/updatecustomfoodpayload)

[`Query.recentFoods`](/reference/2026-01-01/queries/recentfoods)

## Definition

```
"""
A food object
"""
type Food {
  """
  The name of the food creator
  """
  creator_name: String


  """
  first serving size of the food object
  """
  default_serving_size: ServingSize


  """
  The name of the food to display
  """
  display_name: String


  """
  The id of the food in the Edamam database
  """
  edamam_import_id: String


  """
  Whether the food was imported from the FDC database
  """
  fdc_import: Boolean!


  """
  The unique identifier of the food
  """
  id: ID!


  """
  The name of the food
  """
  name: String!


  """
  Nutrients of the food object
  """
  nutrients: [FoodNutrient!]


  """
  Serving sizes of the food object
  """
  serving_sizes: [ServingSize!]


  """
  The ID of the user who created the food
  """
  user_id: String
}
```
