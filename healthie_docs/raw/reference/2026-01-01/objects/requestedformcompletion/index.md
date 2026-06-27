---
title: RequestedFormCompletion | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformcompletion/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformcompletion/index.md
---

A request, from a provider to a client, to fill out a form

## Fields

[`custom_module_form` ](#field-custom-module-form)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· The form to fill out

[`custom_module_form_id` ](#field-custom-module-form-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the form to fill out

[`date_to_show` ](#field-date-to-show)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The relevant date to show, if the form is completed it shows the completed at date, if there is an associated incomplete form it shows when that was started, otherwise shows when the request was created

[`form_answer_group` ](#field-form-answer-group)· [`FormAnswerGroup` ](/reference/2026-01-01/objects/formanswergroup)· The filled form that completes the request

[`form_answer_group_id` ](#field-form-answer-group-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the filled form that completes the request

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the form

[`item_type` ](#field-item-type)· [`String!` ](/reference/2026-01-01/scalars/string)· required · type of form requested

[`metadata` ](#field-metadata)· [`String` ](/reference/2026-01-01/scalars/string)· A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers

[`recipient` ](#field-recipient)· [`User` ](/reference/2026-01-01/objects/user)· The recipient (client)

[`recipient_id` ](#field-recipient-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the recipient (client)

[`recurring_form` ](#field-recurring-form)· [`RecurringForm` ](/reference/2026-01-01/objects/recurringform)· Recurring Form related to the request

[`sender` ](#field-sender)· [`User` ](/reference/2026-01-01/objects/user)· The sender (provider)

[`sender_id` ](#field-sender-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the sender (provider)

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· The status of the request

## Used By

[`FormAnswerGroup.requested_form_completion`](/reference/2026-01-01/objects/formanswergroup)

[`RequestedFormCompletionEdge.node`](/reference/2026-01-01/objects/requestedformcompletionedge)

[`RequestedFormCompletionPaginationConnection.nodes`](/reference/2026-01-01/objects/requestedformcompletionpaginationconnection)

[`createRequestedFormPayload.requestedFormCompletion`](/reference/2026-01-01/objects/createrequestedformpayload)

[`deleteRequestedFormPayload.requestedFormCompletion`](/reference/2026-01-01/objects/deleterequestedformpayload)

[`Query.requestedFormCompletion`](/reference/2026-01-01/queries/requestedformcompletion)

## Definition

```
"""
A request, from a provider to a client, to fill out a form
"""
type RequestedFormCompletion {
  """
  The form to fill out
  """
  custom_module_form: CustomModuleForm


  """
  The ID of the form to fill out
  """
  custom_module_form_id: String


  """
  The relevant date to show, if the form is completed it shows the completed at date, if there is an associated incomplete form it shows when that was started, otherwise shows when the request was created
  """
  date_to_show: ISO8601DateTime


  """
  The filled form that completes the request
  """
  form_answer_group: FormAnswerGroup


  """
  The id of the filled form that completes the request
  """
  form_answer_group_id: String


  """
  The unique identifier of the form
  """
  id: ID!


  """
  type of form requested
  """
  item_type: String!


  """
  A serialized JSON string of metadata. Maximum character limit of 128,000. Only accessible by staff and providers
  """
  metadata: String


  """
  The recipient (client)
  """
  recipient: User


  """
  The ID of the recipient (client)
  """
  recipient_id: String


  """
  Recurring Form related to the request
  """
  recurring_form: RecurringForm


  """
  The sender (provider)
  """
  sender: User


  """
  The ID of the sender (provider)
  """
  sender_id: String


  """
  The status of the request
  """
  status: String
}
```
