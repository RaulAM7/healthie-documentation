---
title: CustomModuleForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleform/index.md
---

A template for a form, that can then be filled out

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date on which the template was created

[`customInstructions` ](#field-custominstructions)· [`String` ](/reference/2026-01-01/scalars/string)· Form-level general instructions passed to AI Scribe alongside the form title (tone, style, structure preferences). Available for charting forms only. Backed by AiScribeFormInstruction so the form schema stays Scribe-agnostic.

[`custom_modules` ](#field-custom-modules)· [`[CustomModule!]!` ](/reference/2026-01-01/objects/custommodule)· required · The questions in the template

[`deleted_at` ](#field-deleted-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date on which the template was deleted

[`external_id` ](#field-external-id)· [`String` ](/reference/2026-01-01/scalars/string)· Custom column used by API users. Used to relate our form objects with objects in third-party systems

[`external_id_type` ](#field-external-id-type)· [`String` ](/reference/2026-01-01/scalars/string)· Custom column used by API users. Used to relate our form objects with objects in third-party systems

[`form_answer_groups` ](#field-form-answer-groups)· [`[FormAnswerGroup!]!` ](/reference/2026-01-01/objects/formanswergroup)· required · All filled out forms for this template

[`has_matrix_field` ](#field-has-matrix-field)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The form has matrix field

[`has_non_readonly_modules` ](#field-has-non-readonly-modules)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the form has modules that the user has to fill out

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the module form

[`is_video` ](#field-is-video)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the form contains only one custom\_module with mod\_type 'video' and was created as part of a program

[`last_updated_by_user` ](#field-last-updated-by-user)· [`User` ](/reference/2026-01-01/objects/user)· User who last updated this form

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 10,000.

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The given name of the template

[`prefill` ](#field-prefill)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether subsequent times filling out the template, will start with the template prefilled with the previous answers

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date on which the template was updated

[`uploaded_by_healthie_team` ](#field-uploaded-by-healthie-team)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether or not this form was uploaded by Healthie team member

[`use_for_charting` ](#field-use-for-charting)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the template can be used to chart with

[`use_for_program` ](#field-use-for-program)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the template was made for a program

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The owner of the template

## Used By

[`AppointmentAutocompleteForm.custom_module_form`](/reference/2026-01-01/objects/appointmentautocompleteform)

[`AppointmentSetting.default_group_charting_template`](/reference/2026-01-01/objects/appointmentsetting)

[`AppointmentTypeFormConnection.custom_module_form`](/reference/2026-01-01/objects/appointmenttypeformconnection)

[`CustomMetric.custom_module_form`](/reference/2026-01-01/objects/custommetric)

[`CustomModule.custom_module_form`](/reference/2026-01-01/objects/custommodule)

[`CustomModuleFormEdge.node`](/reference/2026-01-01/objects/custommoduleformedge)

[`CustomModuleFormPaginationConnection.nodes`](/reference/2026-01-01/objects/custommoduleformpaginationconnection)

[`FormAnswerGroup.custom_module_form`](/reference/2026-01-01/objects/formanswergroup)

[`GeneratedFormAnswerGroupType.custom_module_form`](/reference/2026-01-01/objects/generatedformanswergrouptype)

[`IntakeFlowItem.custom_module_form`](/reference/2026-01-01/objects/intakeflowitem)

[`RecurringForm.custom_module_form`](/reference/2026-01-01/objects/recurringform)

[`RequestedFormCompletion.custom_module_form`](/reference/2026-01-01/objects/requestedformcompletion)

[`SetCustomModuleFormScribeInstructionsPayload.customModuleForm`](/reference/2026-01-01/objects/setcustommoduleformscribeinstructionspayload)

[`copyCustomModuleFormPayload.customModuleForm`](/reference/2026-01-01/objects/copycustommoduleformpayload)

[`createCustomModuleFormPayload.customModuleForm`](/reference/2026-01-01/objects/createcustommoduleformpayload)

[`deleteCustomModuleFormPayload.customModuleForm`](/reference/2026-01-01/objects/deletecustommoduleformpayload)

[`shareCustomModuleFormPayload.customModuleForm`](/reference/2026-01-01/objects/sharecustommoduleformpayload)

[`updateCustomModuleFormPayload.customModuleForm`](/reference/2026-01-01/objects/updatecustommoduleformpayload)

[`Query.customModuleForm`](/reference/2026-01-01/queries/custommoduleform)

## Definition

```
"""
A template for a form, that can then be filled out
"""
type CustomModuleForm {
  """
  The date on which the template was created
  """
  created_at: ISO8601DateTime!


  """
  Form-level general instructions passed to AI Scribe alongside the form title (tone, style, structure preferences). Available for charting forms only. Backed by AiScribeFormInstruction so the form schema stays Scribe-agnostic.
  """
  customInstructions: String


  """
  The questions in the template
  """
  custom_modules: [CustomModule!]!


  """
  The date on which the template was deleted
  """
  deleted_at: ISO8601DateTime


  """
  Custom column used by API users. Used to relate our form objects with objects in third-party systems
  """
  external_id: String


  """
  Custom column used by API users. Used to relate our form objects with objects in third-party systems
  """
  external_id_type: String


  """
  All filled out forms for this template
  """
  form_answer_groups: [FormAnswerGroup!]!


  """
  The form has matrix field
  """
  has_matrix_field: Boolean


  """
  When true, the form has modules that the user has to fill out
  """
  has_non_readonly_modules: Boolean


  """
  The unique identifier of the module form
  """
  id: ID!


  """
  Whether the form contains only one custom_module with mod_type 'video' and was created as part of a program
  """
  is_video: Boolean


  """
  User who last updated this form
  """
  last_updated_by_user: User


  """
  A serialized JSON string of metadata. Maximum character limit of 10,000.
  """
  metadata: String


  """
  The given name of the template
  """
  name: String


  """
  Whether subsequent times filling out the template, will start with the template prefilled with the previous answers
  """
  prefill: Boolean


  """
  The date on which the template was updated
  """
  updated_at: ISO8601DateTime!


  """
  Whether or not this form was uploaded by Healthie team member
  """
  uploaded_by_healthie_team: Boolean!


  """
  Whether the template can be used to chart with
  """
  use_for_charting: Boolean!


  """
  Whether the template was made for a program
  """
  use_for_program: Boolean!


  """
  The owner of the template
  """
  user: User
}
```
