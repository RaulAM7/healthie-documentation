---
title: CustomModuleConditionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleconditiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleconditiontype/index.md
---

Condition under which to show a custom module

## Fields

[`conditional_custom_module_id` ](#field-conditional-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom module whose value determines whether to show or hide the custom module

[`custom_module_id` ](#field-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom module that will be shown or hidden

[`filter_type` ](#field-filter-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of filter

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the condition

[`value_to_filter` ](#field-value-to-filter)· [`String` ](/reference/2026-01-01/scalars/string)· The value to check the filter against

## Used By

[`CustomModule.custom_module_condition`](/reference/2026-01-01/objects/custommodule)

## Definition

```
"""
Condition under which to show a custom module
"""
type CustomModuleConditionType {
  """
  The ID of the custom module whose value determines whether to show or hide the custom module
  """
  conditional_custom_module_id: ID


  """
  The ID of the custom module that will be shown or hidden
  """
  custom_module_id: ID


  """
  The type of filter
  """
  filter_type: String


  """
  The unique identifier of the condition
  """
  id: ID!


  """
  The value to check the filter against
  """
  value_to_filter: String
}
```
