---
title: FormAnswer | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswer/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswer/index.md
---

An answer in a filled form

## Fields

[`answer` ](#field-answer)· [`String` ](/reference/2026-01-01/scalars/string)· The answer to the question

[`conditional_custom_module_id` ](#field-conditional-custom-module-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the custom module whose value determines whether to show or hide the custom module

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The creation time of the form answer

[`custom_module` ](#field-custom-module)· [`CustomModule` ](/reference/2026-01-01/objects/custommodule)· The type of question that was filled out

[`custom_module_id` ](#field-custom-module-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the question template

[`displayed_answer` ](#field-displayed-answer)· [`String` ](/reference/2026-01-01/scalars/string)· The answer to display (some conversions are made verse raw answer data)

[`file_attachments` ](#field-file-attachments)· [`[FileAttachment!]` ](/reference/2026-01-01/objects/fileattachment)· The file attachments associated with this form answer

[`filter_type` ](#field-filter-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of filter

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The filled form that this answer is a part of

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the answer

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label of the question

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000.

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time of the last update

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the user that the answered question is for

[`value_to_filter` ](#field-value-to-filter)· [`String` ](/reference/2026-01-01/scalars/string)· The value to check the filter against

## Used By

[`FormAnswerGroup.form_answers`](/reference/2026-01-01/objects/formanswergroup)

[`Query.initialFormAnswers`](/reference/2026-01-01/queries/initialformanswers)

## Definition

```
"""
An answer in a filled form
"""
type FormAnswer {
  """
  The answer to the question
  """
  answer: String


  """
  The ID of the custom module whose value determines whether to show or hide the custom module
  """
  conditional_custom_module_id: ID


  """
  The creation time of the form answer
  """
  created_at: ISO8601DateTime!


  """
  The type of question that was filled out
  """
  custom_module: CustomModule


  """
  The id of the question template
  """
  custom_module_id: String


  """
  The answer to display (some conversions are made verse raw answer data)
  """
  displayed_answer: String


  """
  The file attachments associated with this form answer
  """
  file_attachments: [FileAttachment!]


  """
  The type of filter
  """
  filter_type: String


  """
  The filled form that this answer is a part of
  """
  form_answer_group: FormAnswerGroup


  """
  The unique identifier of the answer
  """
  id: ID!


  """
  The label of the question
  """
  label: String


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000.
  """
  metadata: String


  """
  The time of the last update
  """
  updated_at: ISO8601DateTime


  """
  The id of the user that the answered question is for
  """
  user_id: String


  """
  The value to check the filter against
  """
  value_to_filter: String
}
```
