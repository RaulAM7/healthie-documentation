---
title: RecurringForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringform/index.md
---

A Recurring Form

## Fields

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· Associated custom module form

[`form_id` ](#field-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the form itself

[`form_type` ](#field-form-type)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The type of form

[`has_connected_recipient` ](#field-has-connected-recipient)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the user or group is connected to the recurring form

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the recurring form

[`interval` ](#field-interval)· [`String` ](/reference/2026-01-01/scalars/string)· The interval of recurrence. Can be: '23:12' / 'Monday, Tuesday' / '31st'

[`interval_type` ](#field-interval-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of recurrence('Daily'(1) / 'Weekly'(2) / 'Monthly'(3))

[`is_active` ](#field-is-active)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the recurrence is active or not

[`recurrence_end_at` ](#field-recurrence-end-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The day when recurrence ends

[`userGroups` ](#field-usergroups)· [`[UserGroup!]` ](/reference/2026-01-01/objects/usergroup)· Get user\_group assigned to the recurring form

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the provider who set up recurrence

[`users` ](#field-users)· [`[User!]` ](/reference/2026-01-01/objects/user)· Get patients assigned to the recurring form

[`users_and_groups` ](#field-users-and-groups)· [`[String]!` ](/reference/2026-01-01/scalars/string)· required · The identifiers of associated users and groups: \['1', '2', 'group-5', 'group-13']

## Used By

[`IntakeFlowItem.recurring_form`](/reference/2026-01-01/objects/intakeflowitem)

[`RecurringFormEdge.node`](/reference/2026-01-01/objects/recurringformedge)

[`RecurringFormPaginationConnection.nodes`](/reference/2026-01-01/objects/recurringformpaginationconnection)

[`RequestedFormCompletion.recurring_form`](/reference/2026-01-01/objects/requestedformcompletion)

[`UserGroup.recurring_forms`](/reference/2026-01-01/objects/usergroup)

[`destroyRecurringFormPayload.recurringForm`](/reference/2026-01-01/objects/destroyrecurringformpayload)

[`updateRecurringFormPayload.recurringForm`](/reference/2026-01-01/objects/updaterecurringformpayload)

## Definition

```
"""
A Recurring Form
"""
type RecurringForm {
  """
  Associated custom module form
  """
  custom_module_form: CustomModuleForm


  """
  The ID of the form itself
  """
  form_id: String


  """
  The type of form
  """
  form_type: String!


  """
  Whether the user or group is connected to the recurring form
  """
  has_connected_recipient(
    """
    The ID of the user or group
    """
    connectable_id: ID


    """
    The type of the user or group
    """
    connectable_type: String
  ): Boolean


  """
  The unique identifier of the recurring form
  """
  id: ID!


  """
  The interval of recurrence. Can be: '23:12' / 'Monday, Tuesday' / '31st'
  """
  interval: String


  """
  The type of recurrence('Daily'(1) / 'Weekly'(2) / 'Monthly'(3))
  """
  interval_type: String


  """
  Whether the recurrence is active or not
  """
  is_active: Boolean!


  """
  The day when recurrence ends
  """
  recurrence_end_at: ISO8601DateTime


  """
  Get user_group assigned to the recurring form
  """
  userGroups: [UserGroup!]


  """
  The ID of the provider who set up recurrence
  """
  user_id: String


  """
  Get patients assigned to the recurring form
  """
  users: [User!]


  """
  The identifiers of associated users and groups: ['1', '2', 'group-5', 'group-13']
  """
  users_and_groups: [String]!
}
```
