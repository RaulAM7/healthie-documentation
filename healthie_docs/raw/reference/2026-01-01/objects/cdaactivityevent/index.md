---
title: CdaActivityEvent | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cdaactivityevent/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cdaactivityevent/index.md
---

Information on an event surrounding CDA activity

## Fields

[`activity_type` ](#field-activity-type)· [`String` ](/reference/2026-01-01/scalars/string)· The activity that occured

[`cda_type` ](#field-cda-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of CDA

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time of the event

[`document_id` ](#field-document-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the document

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Self descriptive

[`outbound_recipient` ](#field-outbound-recipient)· [`String` ](/reference/2026-01-01/scalars/string)· The outbound recipient

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· The user who opened the document

[`user_email` ](#field-user-email)· [`String` ](/reference/2026-01-01/scalars/string)· The email of the user who took the action.

## Used By

[`CdaActivityEventEdge.node`](/reference/2026-01-01/objects/cdaactivityeventedge)

[`CdaActivityEventPaginationConnection.nodes`](/reference/2026-01-01/objects/cdaactivityeventpaginationconnection)

## Definition

```
"""
Information on an event surrounding CDA activity
"""
type CdaActivityEvent {
  """
  The activity that occured
  """
  activity_type: String


  """
  The type of CDA
  """
  cda_type: String


  """
  The time of the event
  """
  created_at: ISO8601DateTime


  """
  The ID of the document
  """
  document_id: String


  """
  Self descriptive
  """
  id: ID!


  """
  The outbound recipient
  """
  outbound_recipient: String


  """
  The user who opened the document
  """
  user: User


  """
  The email of the user who took the action.
  """
  user_email: String
}
```
