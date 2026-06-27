---
title: CustomEmail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/customemail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/customemail/index.md
---

A custom email

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · created at

[`email_type` ](#field-email-type)· [`String` ](/reference/2026-01-01/scalars/string)· type of email

[`greeting` ](#field-greeting)· [`String` ](/reference/2026-01-01/scalars/string)· email greeting

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the email

[`message_body` ](#field-message-body)· [`String` ](/reference/2026-01-01/scalars/string)· message body

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· subject of email

[`reactivation_wait_days` ](#field-reactivation-wait-days)· [`String` ](/reference/2026-01-01/scalars/string)· reactivation\_wait\_days

[`related_object` ](#field-related-object)· [`CustomEmailRelatedObject` ](/reference/2026-01-01/unions/customemailrelatedobject)· Appointment Type, Program or Package object

[`subject` ](#field-subject)· [`String` ](/reference/2026-01-01/scalars/string)· subject of email

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · updated at

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· user id of provider

## Used By

[`CustomEmailEdge.node`](/reference/2026-01-01/objects/customemailedge)

[`CustomEmailPaginationConnection.nodes`](/reference/2026-01-01/objects/customemailpaginationconnection)

[`User.custom_custom_emails`](/reference/2026-01-01/objects/user)

[`User.reactivation_emails`](/reference/2026-01-01/objects/user)

[`createCustomEmailPayload.customEmail`](/reference/2026-01-01/objects/createcustomemailpayload)

[`deleteCustomEmailPayload.customEmail`](/reference/2026-01-01/objects/deletecustomemailpayload)

[`updateCustomEmailPayload.customEmail`](/reference/2026-01-01/objects/updatecustomemailpayload)

[`Query.customEmail`](/reference/2026-01-01/queries/customemail)

## Definition

```
"""
A custom email
"""
type CustomEmail {
  """
  created at
  """
  created_at: ISO8601DateTime!


  """
  type of email
  """
  email_type: String


  """
  email greeting
  """
  greeting: String


  """
  The unique identifier of the email
  """
  id: ID!


  """
  message body
  """
  message_body: String


  """
  subject of email
  """
  name: String


  """
  reactivation_wait_days
  """
  reactivation_wait_days: String


  """
  Appointment Type, Program or Package object
  """
  related_object: CustomEmailRelatedObject


  """
  subject of email
  """
  subject: String


  """
  updated at
  """
  updated_at: ISO8601DateTime!


  """
  user id of provider
  """
  user_id: ID
}
```
