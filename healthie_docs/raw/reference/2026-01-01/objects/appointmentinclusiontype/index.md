---
title: AppointmentInclusionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentinclusiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentinclusiontype/index.md
---

Provider/Client to Appointment connection

## Fields

[`appointment` ](#field-appointment)· [`Appointment` ](/reference/2026-01-01/objects/appointment)· The appointment the inclusion is connected to.

[`attended` ](#field-attended)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicate whether a group appointment attendee have taken part in the appointment

[`cancellation_reason` ](#field-cancellation-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The reason for cancellation if the appointment was cancelled

[`cancelled` ](#field-cancelled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Indicate if a group appointment attendee cancelled the appointment

[`cancelled_at` ](#field-cancelled-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The timestamp of when the attendee cancelled the appointment

[`cancelled_by` ](#field-cancelled-by)· [`User` ](/reference/2026-01-01/objects/user)· The user who performed the cancellation

[`cancelled_by_id` ](#field-cancelled-by-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the user who performed the cancellation

[`confirmed` ](#field-confirmed)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the client has confirmed the appointment, or don't need to (THIS IS FIELD IS CURRENTLY USED ONLY FOR GROUP APPT's)

[`external_uuid` ](#field-external-uuid)· [`ID` ](/reference/2026-01-01/scalars/id)· The UUID of the appointment inclusion. Can be used in conjunction with appointment settings to allow unauthenticated users to modify an appointment.

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the appointment inclusion

[`join_time` ](#field-join-time)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The datetime that the attendee joined the appointment

[`leave_time` ](#field-leave-time)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The datetime that the attendee left the appointment

[`other_cancellation_reason` ](#field-other-cancellation-reason)· [`String` ](/reference/2026-01-01/scalars/string)· The other reason for cancellation if the appointment was cancelled

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Attendee

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Attendee ID

deprecated

Use \`user\` field

## Used By

[`Appointment.attended_clients`](/reference/2026-01-01/objects/appointment)

[`updateAppointmentInclusionPayload.appointment_inclusion`](/reference/2026-01-01/objects/updateappointmentinclusionpayload)

[`Query.appointmentInclusion`](/reference/2026-01-01/queries/appointmentinclusion)

## Definition

```
"""
Provider/Client to Appointment connection
"""
type AppointmentInclusionType {
  """
  The appointment the inclusion is connected to.
  """
  appointment: Appointment


  """
  Indicate whether a group appointment attendee have taken part in the appointment
  """
  attended: Boolean


  """
  The reason for cancellation if the appointment was cancelled
  """
  cancellation_reason: String


  """
  Indicate if a group appointment attendee cancelled the appointment
  """
  cancelled: Boolean


  """
  The timestamp of when the attendee cancelled the appointment
  """
  cancelled_at: ISO8601DateTime


  """
  The user who performed the cancellation
  """
  cancelled_by: User


  """
  The ID of the user who performed the cancellation
  """
  cancelled_by_id: ID


  """
  If the client has confirmed the appointment, or don't need to (THIS IS FIELD IS CURRENTLY USED ONLY FOR GROUP APPT's)
  """
  confirmed: Boolean


  """
  The UUID of the appointment inclusion. Can be used in conjunction with appointment settings to allow unauthenticated users to modify an appointment.
  """
  external_uuid: ID


  """
  The unique identifier of the appointment inclusion
  """
  id: ID!


  """
  The datetime that the attendee joined the appointment
  """
  join_time: ISO8601DateTime


  """
  The datetime that the attendee left the appointment
  """
  leave_time: ISO8601DateTime


  """
  The other reason for cancellation if the appointment was cancelled
  """
  other_cancellation_reason: String


  """
  Attendee
  """
  user: User


  """
  Attendee ID
  """
  user_id: ID @deprecated(reason: "Use `user` field")
}
```
