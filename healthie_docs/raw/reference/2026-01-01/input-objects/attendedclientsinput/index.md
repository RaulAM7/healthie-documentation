---
title: AttendedClientsInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/attendedclientsinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/attendedclientsinput/index.md
---

Payload for an AttendedClient

## Fields

[`attended` ](#field-attended)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the client attended the event

[`cancelled` ](#field-cancelled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the client cancelled the event

[`cancellation_reason` ](#field-cancellation-reason)· [`String` ](/reference/2026-01-01/scalars/string)· Reason for cancellation

[`other_cancellation_reason` ](#field-other-cancellation-reason)· [`String` ](/reference/2026-01-01/scalars/string)· Other reason for cancellation

[`confirmed` ](#field-confirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the client confirmed the event

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the object

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user

## Used By

[`updateAppointmentInput.attended_clients`](/reference/2026-01-01/input-objects/updateappointmentinput)

## Definition

```
"""
Payload for an AttendedClient
"""
input AttendedClientsInput {
  """
  If the client attended the event
  """
  attended: Boolean


  """
  If the client cancelled the event
  """
  cancelled: Boolean


  """
  Reason for cancellation
  """
  cancellation_reason: String


  """
  Other reason for cancellation
  """
  other_cancellation_reason: String


  """
  If the client confirmed the event
  """
  confirmed: Boolean


  """
  The unique identifier of the object
  """
  id: ID


  """
  The ID of the user
  """
  user_id: ID
}
```
