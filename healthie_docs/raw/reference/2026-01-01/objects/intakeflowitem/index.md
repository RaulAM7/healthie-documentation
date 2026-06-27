---
title: IntakeFlowItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/intakeflowitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/intakeflowitem/index.md
---

The intake flow item

## Fields

[`attached_object_edit_url` ](#field-attached-object-edit-url)· [`String` ](/reference/2026-01-01/scalars/string)· Attached object

[`completed_onboarding_item` ](#field-completed-onboarding-item)· [`CompletedOnboardingItem` ](/reference/2026-01-01/objects/completedonboardingitem)· The completed onboarding item for the given user id (from args)

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· The form to fill out

[`date_to_show` ](#field-date-to-show)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The relevant date to show

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The display name

[`form_answer_group_id` ](#field-form-answer-group-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the filled form that completes the request. Only present if form\_type is RequestedForm

[`form_type` ](#field-form-type)· [`String` ](/reference/2026-01-01/scalars/string)· Form type

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique idenitifier of the item

[`incomplete_form_id` ](#field-incomplete-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· Return the ID of the incomplete form

[`item_type` ](#field-item-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of item

[`onboarding_item` ](#field-onboarding-item)· [`OnboardingItem` ](/reference/2026-01-01/objects/onboardingitem)· The onboarding item that was completed

[`recurring_form` ](#field-recurring-form)· [`RecurringForm` ](/reference/2026-01-01/objects/recurringform)· Recurring form related to the request

[`request_info` ](#field-request-info)· [`IntakeFlowItemRequestInfo` ](/reference/2026-01-01/objects/intakeflowitemrequestinfo)· The intake flow item request details

[`skipped` ](#field-skipped)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Skipped

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Form status

[`tab_type` ](#field-tab-type)· [`String` ](/reference/2026-01-01/scalars/string)· Tab type

[`typename` ](#field-typename)· [`String` ](/reference/2026-01-01/scalars/string)· Corrected typename of the intake flow item object

[`view_url` ](#field-view-url)· [`String` ](/reference/2026-01-01/scalars/string)· View url

## Used By

[`IntakeFlowType.all_forms`](/reference/2026-01-01/objects/intakeflowtype)

[`IntakeFlowType.completed_skipped`](/reference/2026-01-01/objects/intakeflowtype)

[`IntakeFlowType.forms`](/reference/2026-01-01/objects/intakeflowtype)

[`IntakeFlowType.intake_flows`](/reference/2026-01-01/objects/intakeflowtype)

[`IntakeFlowType.not_started_incomplete`](/reference/2026-01-01/objects/intakeflowtype)

[`IntakeFlowType.requested`](/reference/2026-01-01/objects/intakeflowtype)

## Definition

```
"""
The intake flow item
"""
type IntakeFlowItem {
  """
  Attached object
  """
  attached_object_edit_url: String


  """
  The completed onboarding item for the given user id (from args)
  """
  completed_onboarding_item: CompletedOnboardingItem


  """
  The form to fill out
  """
  custom_module_form: CustomModuleForm


  """
  The relevant date to show
  """
  date_to_show: ISO8601DateTime


  """
  The display name
  """
  display_name: String


  """
  The id of the filled form that completes the request. Only present if form_type is RequestedForm
  """
  form_answer_group_id: String


  """
  Form type
  """
  form_type: String


  """
  The unique idenitifier of the item
  """
  id: ID!


  """
  Return the ID of the incomplete form
  """
  incomplete_form_id: String


  """
  The type of item
  """
  item_type: String


  """
  The onboarding item that was completed
  """
  onboarding_item: OnboardingItem


  """
  Recurring form related to the request
  """
  recurring_form: RecurringForm


  """
  The intake flow item request details
  """
  request_info: IntakeFlowItemRequestInfo


  """
  Skipped
  """
  skipped: Boolean


  """
  Form status
  """
  status: String


  """
  Tab type
  """
  tab_type: String


  """
  Corrected typename of the intake flow item object
  """
  typename: String


  """
  View url
  """
  view_url: String
}
```
