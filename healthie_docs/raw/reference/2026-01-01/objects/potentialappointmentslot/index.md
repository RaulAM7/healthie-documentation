---
title: PotentialAppointmentSlot | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/potentialappointmentslot/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/potentialappointmentslot/index.md
---

A potential appointment slot

## Fields

[`appointment_id` ](#field-appointment-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the appointment this slot is for

[`appointment_type` ](#field-appointment-type)· [`AppointmentType` ](/reference/2026-01-01/objects/appointmenttype)· The type of appointment the slot is for. Returns nil if not a group appointment. Returning this for many slots can potentially slow down query times.

[`color` ](#field-color)· [`String` ](/reference/2026-01-01/scalars/string)· The hexcode color of the slot (Not used in Healthie's default self-scheduling widget)

[`date` ](#field-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date of the slot

[`has_waitlist_enabled` ](#field-has-waitlist-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether this slot has waitlist enabled

[`is_fully_booked` ](#field-is-fully-booked)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether this slot is fully booked

[`length` ](#field-length)· [`Int` ](/reference/2026-01-01/scalars/int)· The length of the appointment type (in minutes)

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user who owns the slot

## Used By

[`Query.availableSlotsForRange`](/reference/2026-01-01/queries/availableslotsforrange)

## Definition

```
"""
A potential appointment slot
"""
type PotentialAppointmentSlot {
  """
  The ID of the appointment this slot is for
  """
  appointment_id: String


  """
  The type of appointment the slot is for. Returns nil if not a group appointment. Returning this for many slots can potentially slow down query times.
  """
  appointment_type: AppointmentType


  """
  The hexcode color of the slot (Not used in Healthie's default self-scheduling widget)
  """
  color: String


  """
  The date of the slot
  """
  date: ISO8601DateTime


  """
  Whether this slot has waitlist enabled
  """
  has_waitlist_enabled: Boolean


  """
  Whether this slot is fully booked
  """
  is_fully_booked: Boolean


  """
  The length of the appointment type (in minutes)
  """
  length: Int


  """
  The ID of the user who owns the slot
  """
  user_id: String
}
```
