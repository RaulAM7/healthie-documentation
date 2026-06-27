---
title: NutrientsInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/nutrientsinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/nutrientsinput/index.md
---

Payload for a food nutrients

## Fields

[`added_sugars` ](#field-added-sugars)· [`String` ](/reference/2026-01-01/scalars/string)· The number of added sugars in the food

[`calcium` ](#field-calcium)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of calcium in the food

[`carbs` ](#field-carbs)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of carbohydrates in the food

[`cholesterol` ](#field-cholesterol)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of cholesterol in the food

[`fat` ](#field-fat)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of fat in the food

[`iron` ](#field-iron)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of iron in the food

[`kcal` ](#field-kcal)· [`String` ](/reference/2026-01-01/scalars/string)· The number of kilocalories in the food

[`monounsaturated_fat` ](#field-monounsaturated-fat)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of monounsaturated fat in the food

[`polyunsaturated_fat` ](#field-polyunsaturated-fat)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of polyunsaturated fat in the food

[`potassium` ](#field-potassium)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of potassium in the food

[`protein` ](#field-protein)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of protein in the food

[`saturated_fat` ](#field-saturated-fat)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of saturated fat in the food

[`sodium` ](#field-sodium)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of sodium in the food

[`total_fiber` ](#field-total-fiber)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of total fiber in the food

[`total_sugars` ](#field-total-sugars)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of total sugars in the food

[`trans_fat` ](#field-trans-fat)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of trans fat in the food

[`vitamin_a` ](#field-vitamin-a)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of vitamin A in the food

[`vitamin_c` ](#field-vitamin-c)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of vitamin C in the food

[`vitamin_d` ](#field-vitamin-d)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of vitamin D in the food

## Used By

[`createCustomFoodInput.nutrients`](/reference/2026-01-01/input-objects/createcustomfoodinput)

[`updateCustomFoodInput.nutrients`](/reference/2026-01-01/input-objects/updatecustomfoodinput)

## Definition

```
"""
Payload for a food nutrients
"""
input NutrientsInput {
  """
  The number of added sugars in the food
  """
  added_sugars: String


  """
  The amount of calcium in the food
  """
  calcium: String


  """
  The amount of carbohydrates in the food
  """
  carbs: String


  """
  The amount of cholesterol in the food
  """
  cholesterol: String


  """
  The amount of fat in the food
  """
  fat: String


  """
  The amount of iron in the food
  """
  iron: String


  """
  The number of kilocalories in the food
  """
  kcal: String


  """
  The amount of monounsaturated fat in the food
  """
  monounsaturated_fat: String


  """
  The amount of polyunsaturated fat in the food
  """
  polyunsaturated_fat: String


  """
  The amount of potassium in the food
  """
  potassium: String


  """
  The amount of protein in the food
  """
  protein: String


  """
  The amount of saturated fat in the food
  """
  saturated_fat: String


  """
  The amount of sodium in the food
  """
  sodium: String


  """
  The amount of total fiber in the food
  """
  total_fiber: String


  """
  The amount of total sugars in the food
  """
  total_sugars: String


  """
  The amount of trans fat in the food
  """
  trans_fat: String


  """
  The amount of vitamin A in the food
  """
  vitamin_a: String


  """
  The amount of vitamin C in the food
  """
  vitamin_c: String


  """
  The amount of vitamin D in the food
  """
  vitamin_d: String
}
```
