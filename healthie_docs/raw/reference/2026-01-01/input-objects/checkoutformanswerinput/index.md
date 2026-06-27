---
title: CheckoutFormAnswerInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/checkoutformanswerinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/checkoutformanswerinput/index.md
---

Payload for an answer

## Fields

[`answer` ](#field-answer)· [`String` ](/reference/2026-01-01/scalars/string)· The answer

[`conditional_custom_module_id` ](#field-conditional-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom module

[`custom_module_id` ](#field-custom-module-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the custom module

[`filter_type` ](#field-filter-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the filter

[`mod_type` ](#field-mod-type)· [`String` ](/reference/2026-01-01/scalars/string)· The mod\_type (e.g question type) that is being answered.

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Unique ID for the answer

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label for the answer

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user who created the answer

[`value_to_filter` ](#field-value-to-filter)· [`String` ](/reference/2026-01-01/scalars/string)· The value to filter on

## Used By

[`CheckoutFormAnswerGroupInput.form_answers`](/reference/2026-01-01/input-objects/checkoutformanswergroupinput)

## Definition

```
"""
Payload for an answer
"""
input CheckoutFormAnswerInput {
  """
  The answer
  """
  answer: String


  """
  The ID of the custom module
  """
  conditional_custom_module_id: ID


  """
  The ID of the custom module
  """
  custom_module_id: String


  """
  The type of the filter
  """
  filter_type: String


  """
  The mod_type (e.g question type) that is being answered.
  """
  mod_type: String


  """
  Unique ID for the answer
  """
  id: ID


  """
  The label for the answer
  """
  label: String


  """
  The ID of the user who created the answer
  """
  user_id: String


  """
  The value to filter on
  """
  value_to_filter: String
}
```
