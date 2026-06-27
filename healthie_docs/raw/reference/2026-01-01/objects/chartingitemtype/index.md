---
title: ChartingItemType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chartingitemtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chartingitemtype/index.md
---

Charting Item

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date of the item' creation

[`custom_module_form_name` ](#field-custom-module-form-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the custom module form

[`document` ](#field-document)· [`Document` ](/reference/2026-01-01/objects/document)· The type of the document

[`filler_id` ](#field-filler-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the filler

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The type of the form answer group

[`form_answer_group_id` ](#field-form-answer-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the form answer group

[`generated_form_answer_group` ](#field-generated-form-answer-group)· [`GeneratedFormAnswerGroupType` ](/reference/2026-01-01/objects/generatedformanswergrouptype)· The type of the generated form answer group

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the item

[`is_document` ](#field-is-document)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the item is a document

[`is_generated` ](#field-is-generated)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the item is generated

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the item

[`provider_name` ](#field-provider-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the provider

[`signed` ](#field-signed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the item is signed

[`use_for_charting` ](#field-use-for-charting)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the item is used for a charting

[`use_for_program` ](#field-use-for-program)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the item is used for a program

## Used By

[`Query.chartingItems`](/reference/2026-01-01/queries/chartingitems)

## Definition

```
"""
Charting Item
"""
type ChartingItemType {
  """
  The date of the item' creation
  """
  created_at: ISO8601DateTime!


  """
  The name of the custom module form
  """
  custom_module_form_name: String


  """
  The type of the document
  """
  document: Document


  """
  The ID of the filler
  """
  filler_id: ID


  """
  The type of the form answer group
  """
  form_answer_group: FormAnswerGroup


  """
  The ID of the form answer group
  """
  form_answer_group_id: ID


  """
  The type of the generated form answer group
  """
  generated_form_answer_group: GeneratedFormAnswerGroupType


  """
  The unique identifier of the item
  """
  id: ID!


  """
  Whether the item is a document
  """
  is_document: Boolean


  """
  Whether the item is generated
  """
  is_generated: Boolean


  """
  The name of the item
  """
  name: String


  """
  The name of the provider
  """
  provider_name: String


  """
  Whether the item is signed
  """
  signed: Boolean


  """
  Whether the item is used for a charting
  """
  use_for_charting: Boolean


  """
  Whether the item is used for a program
  """
  use_for_program: Boolean
}
```
