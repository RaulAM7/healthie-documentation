---
title: FormAnswerInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/formanswerinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/formanswerinput/index.md
---

Payload for an answer

## Fields

[`answer` ](#field-answer)· [`String` ](/reference/2026-01-01/scalars/string)· The answer

[`conditional_custom_module_id` ](#field-conditional-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the conditional custom module

[`custom_module_id` ](#field-custom-module-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the custom module

[`filter_type` ](#field-filter-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of filter

[`mod_type` ](#field-mod-type)· [`String` ](/reference/2026-01-01/scalars/string)· (CURRENTLY UNUSED) The mod\_type (e.g question type) that is being answered.

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000.

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Unique ID for the answer

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label for the answer

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user who created the answer

[`value_to_filter` ](#field-value-to-filter)· [`String` ](/reference/2026-01-01/scalars/string)· The value to filter by

## Used By

[`CreateClientViaFormInput.form_answers`](/reference/2026-01-01/input-objects/createclientviaforminput)

[`createFormAnswerGroupInput.form_answers`](/reference/2026-01-01/input-objects/createformanswergroupinput)

[`updateFormAnswerGroupInput.form_answers`](/reference/2026-01-01/input-objects/updateformanswergroupinput)

## Definition

```
"""
Payload for an answer
"""
input FormAnswerInput {
  """
  The answer
  """
  answer: String


  """
  The ID of the conditional custom module
  """
  conditional_custom_module_id: ID


  """
  The ID of the custom module
  """
  custom_module_id: String


  """
  The type of filter
  """
  filter_type: String


  """
  (CURRENTLY UNUSED) The mod_type (e.g question type) that is being answered.
  """
  mod_type: String


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000.
  """
  metadata: String


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
  The value to filter by
  """
  value_to_filter: String
}
```
