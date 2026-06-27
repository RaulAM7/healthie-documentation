---
title: RecurringAppointment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringappointment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringappointment/index.md
---

A Recurring Appointment

## Fields

[`appointments` ](#field-appointments)· [`AppointmentPaginationConnection` ](/reference/2026-01-01/objects/appointmentpaginationconnection)· All appointments for recurring appointment

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the recurring appointment

[`join_all` ](#field-join-all)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Auto-register clients for all appointments in series

[`previous_recurring_appointment_id` ](#field-previous-recurring-appointment-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the previous recurring appointment if this was split from another

[`repeat_interval` ](#field-repeat-interval)· [`String` ](/reference/2026-01-01/scalars/string)· Interval between each appointment in the series

[`repeat_times` ](#field-repeat-times)· [`String` ](/reference/2026-01-01/scalars/string)· Count of the appointment recurrences

## Used By

[`Appointment.recurring_appointment`](/reference/2026-01-01/objects/appointment)

[`Query.recurringAppointment`](/reference/2026-01-01/queries/recurringappointment)

## Definition

```
"""
A Recurring Appointment
"""
type RecurringAppointment {
  """
  All appointments for recurring appointment
  """
  appointments(
    """
    Returns the elements in the list that come after the specified cursor.
    """
    after: String


    """
    Returns the elements in the list that come before the specified cursor.
    """
    before: String


    """
    Returns the first _n_ elements from the list.
    """
    first: Int


    """
    Returns the last _n_ elements from the list.
    """
    last: Int
    order_by: AppointmentOrderKeys = DATE_ASC
  ): AppointmentPaginationConnection


  """
  The unique identifier of the recurring appointment
  """
  id: ID!


  """
  Auto-register clients for all appointments in series
  """
  join_all: Boolean!


  """
  The ID of the previous recurring appointment if this was split from another
  """
  previous_recurring_appointment_id: ID


  """
  Interval between each appointment in the series
  """
  repeat_interval: String


  """
  Count of the appointment recurrences
  """
  repeat_times: String
}
```
