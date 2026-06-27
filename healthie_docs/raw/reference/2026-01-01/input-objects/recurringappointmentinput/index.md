---
title: RecurringAppointmentInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/recurringappointmentinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/recurringappointmentinput/index.md
---

Payload for a recurring appointment

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the recurring appointment

[`join_all` ](#field-join-all)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, all appointments will be joined into one appointment

[`repeat_interval` ](#field-repeat-interval)· [`String` ](/reference/2026-01-01/scalars/string)· Options are \["Weekly", "Biweekly", "Monthly", or "Every 4 Weeks"]

[`repeat_times` ](#field-repeat-times)· [`String` ](/reference/2026-01-01/scalars/string)· Must be a positive number. For example, the following values are valid: "2", "10", "25", "52"

## Used By

[`createAppointmentInput.recurring_appointment`](/reference/2026-01-01/input-objects/createappointmentinput)

[`updateAppointmentInput.recurring_appointment`](/reference/2026-01-01/input-objects/updateappointmentinput)

## Definition

```
"""
Payload for a recurring appointment
"""
input RecurringAppointmentInput {
  """
  The unique identifier of the recurring appointment
  """
  id: ID


  """
  If true, all appointments will be joined into one appointment
  """
  join_all: Boolean = false


  """
  Options are ["Weekly", "Biweekly", "Monthly", or "Every 4 Weeks"]
  """
  repeat_interval: String


  """
  Must be a positive number. For example, the following values are valid: "2", "10", "25", "52"
  """
  repeat_times: String
}
```
