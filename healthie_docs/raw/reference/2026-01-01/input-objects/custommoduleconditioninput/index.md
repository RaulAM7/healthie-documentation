---
title: CustomModuleConditionInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/custommoduleconditioninput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/custommoduleconditioninput/index.md
---

Payload for a CustomModuleCondition

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the condition will be deleted

[`conditional_custom_module_id` ](#field-conditional-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the CustomModule that will be shown if the condition is met

[`filter_type` ](#field-filter-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of filter to apply to the CustomModuleCondition

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the CustomModuleCondition

[`value_to_filter` ](#field-value-to-filter)· [`String` ](/reference/2026-01-01/scalars/string)· The value to filter by

## Used By

[`updateCustomModuleInput.custom_module_condition`](/reference/2026-01-01/input-objects/updatecustommoduleinput)

## Definition

```
"""
Payload for a CustomModuleCondition
"""
input CustomModuleConditionInput {
  """
  If true, the condition will be deleted
  """
  _destroy: Boolean


  """
  The ID of the CustomModule that will be shown if the condition is met
  """
  conditional_custom_module_id: ID


  """
  The type of filter to apply to the CustomModuleCondition
  """
  filter_type: String


  """
  The ID of the CustomModuleCondition
  """
  id: ID


  """
  The value to filter by
  """
  value_to_filter: String
}
```
