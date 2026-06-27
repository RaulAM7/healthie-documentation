---
title: ServingSizeInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/servingsizeinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/servingsizeinput/index.md
---

The serving size of a food

## Fields

[`amount` ](#field-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The amount of the serving size

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the serving size

[`unit` ](#field-unit)· [`String` ](/reference/2026-01-01/scalars/string)· The unit of the serving size

## Used By

[`createCustomFoodInput.serving_size`](/reference/2026-01-01/input-objects/createcustomfoodinput)

[`updateCustomFoodInput.serving_size`](/reference/2026-01-01/input-objects/updatecustomfoodinput)

## Definition

```
"""
The serving size of a food
"""
input ServingSizeInput {
  """
  The amount of the serving size
  """
  amount: String


  """
  The id of the serving size
  """
  id: ID


  """
  The unit of the serving size
  """
  unit: String
}
```
