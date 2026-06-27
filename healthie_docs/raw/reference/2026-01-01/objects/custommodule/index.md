---
title: CustomModule | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommodule/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommodule/index.md
---

A question in a template

## Fields

[`controls_conditional_modules` ](#field-controls-conditional-modules)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· True if there are conditionally displayed custom modules which rely on state of this module

[`copied_from_form_name` ](#field-copied-from-form-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the form this custom module has been originally copied from

[`custom_module_condition` ](#field-custom-module-condition)· [`CustomModuleConditionType` ](/reference/2026-01-01/objects/custommoduleconditiontype)· The conditional logic for showing/hiding the custom module

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· The template that this question is a part of

[`custom_module_form_id` ](#field-custom-module-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the template the question is a part of

[`custom_module_form_section_id` ](#field-custom-module-form-section-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the form section this custom module belongs to. Used for autoscoring

[`exclude_from_scribe` ](#field-exclude-from-scribe)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, this field is stripped from the AI Scribe LLM payload and its original value is preserved after the Scribe response

[`external_id` ](#field-external-id)· [`String` ](/reference/2026-01-01/scalars/string)· Custom column used by API users. Used to relate our form objects with objects in third-party systems

[`external_id_type` ](#field-external-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· Custom column used by API users. Used to relate our form objects with objects in third-party systems

[`file_attachment` ](#field-file-attachment)· [`FileAttachment` ](/reference/2026-01-01/objects/fileattachment)· The image attachment for this custom module. Only returns a value when mod\_type is "image" and an image has been attached.

[`hipaa_name` ](#field-hipaa-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name to use in the HIPAA form

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the module

[`is_custom` ](#field-is-custom)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether this module is a custom module

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label of the question

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000.

[`mod_type` ](#field-mod-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of question

[`options` ](#field-options)· [`String` ](/reference/2026-01-01/scalars/string)· The default options for this question

[`options_array` ](#field-options-array)· [`[String]` ](/reference/2026-01-01/scalars/string)· The options, broken up into an array

[`other_module_ids_to_autoscore_on` ](#field-other-module-ids-to-autoscore-on)· [`[ID]` ](/reference/2026-01-01/scalars/id)· IDs of of other modules to include in the autoscore calculation

[`parent_custom_module_id` ](#field-parent-custom-module-id)· [`String` ](/reference/2026-01-01/scalars/string)· ID of the parent custom module

[`position` ](#field-position)· [`Float` ](/reference/2026-01-01/scalars/float)· The position of the question (the lower the earlier the question is shown)

[`position_integer` ](#field-position-integer)· [`Int` ](/reference/2026-01-01/scalars/int)· Eventually will replace position, currently unused. The position of the question (the lower the earlier the question is shown)

[`required` ](#field-required)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether this question is required to be completed before the form it's in can be saved

[`sublabel` ](#field-sublabel)· [`String` ](/reference/2026-01-01/scalars/string)· The sublabel (description) of the question

## Used By

[`CustomModuleEdge.node`](/reference/2026-01-01/objects/custommoduleedge)

[`CustomModuleForm.custom_modules`](/reference/2026-01-01/objects/custommoduleform)

[`CustomModulePaginationConnection.nodes`](/reference/2026-01-01/objects/custommodulepaginationconnection)

[`FormAnswer.custom_module`](/reference/2026-01-01/objects/formanswer)

[`GeneratedFormAnswerType.custom_module`](/reference/2026-01-01/objects/generatedformanswertype)

[`copyCustomModulePayload.customModule`](/reference/2026-01-01/objects/copycustommodulepayload)

[`createCustomModulePayload.customModule`](/reference/2026-01-01/objects/createcustommodulepayload)

[`deleteCustomModulePayload.customModule`](/reference/2026-01-01/objects/deletecustommodulepayload)

[`updateCustomModulePayload.customModule`](/reference/2026-01-01/objects/updatecustommodulepayload)

[`Query.questionBankModules`](/reference/2026-01-01/queries/questionbankmodules)

## Definition

```
"""
A question in a template
"""
type CustomModule {
  """
  True if there are conditionally displayed custom modules which rely on state of this module
  """
  controls_conditional_modules: Boolean


  """
  The name of the form this custom module has been originally copied from
  """
  copied_from_form_name: String


  """
  The conditional logic for showing/hiding the custom module
  """
  custom_module_condition: CustomModuleConditionType


  """
  The template that this question is a part of
  """
  custom_module_form: CustomModuleForm


  """
  The ID of the template the question is a part of
  """
  custom_module_form_id: String


  """
  The ID of the form section this custom module belongs to. Used for autoscoring
  """
  custom_module_form_section_id: ID


  """
  When true, this field is stripped from the AI Scribe LLM payload and its original value is preserved after the Scribe response
  """
  exclude_from_scribe: Boolean!


  """
  Custom column used by API users. Used to relate our form objects with objects in third-party systems
  """
  external_id: String


  """
  Custom column used by API users. Used to relate our form objects with objects in third-party systems
  """
  external_id_type: String


  """
  The image attachment for this custom module. Only returns a value when mod_type is "image" and an image has been attached.
  """
  file_attachment: FileAttachment


  """
  The name to use in the HIPAA form
  """
  hipaa_name: String


  """
  The unique identifier of the module
  """
  id: ID!


  """
  Whether this module is a custom module
  """
  is_custom: Boolean!


  """
  The label of the question
  """
  label: String


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000.
  """
  metadata: String


  """
  The type of question
  """
  mod_type: String


  """
  The default options for this question
  """
  options: String


  """
  The options, broken up into an array
  """
  options_array: [String]


  """
  IDs of of other modules to include in the autoscore calculation
  """
  other_module_ids_to_autoscore_on: [ID]


  """
  ID of the parent custom module
  """
  parent_custom_module_id: String


  """
  The position of the question (the lower the earlier the question is shown)
  """
  position: Float


  """
  Eventually will replace position, currently unused. The position of the question (the lower the earlier the question is shown)
  """
  position_integer: Int


  """
  Whether this question is required to be completed before the form it's in can be saved
  """
  required: Boolean


  """
  The sublabel (description) of the question
  """
  sublabel: String
}
```
