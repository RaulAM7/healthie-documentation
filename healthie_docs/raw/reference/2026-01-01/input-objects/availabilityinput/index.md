---
title: AvailabilityInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/availabilityinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/availabilityinput/index.md
---

Payload for an availability

## Fields

[`appointment_location_id` ](#field-appointment-location-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the appointment location

[`appointment_type_id` ](#field-appointment-type-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the appointment type

[`contact_type_id` ](#field-contact-type-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the contact type

[`day_of_week` ](#field-day-of-week)· [`Int` ](/reference/2026-01-01/scalars/int)· The day of the week for the availability

[`end_time` ](#field-end-time)· [`String` ](/reference/2026-01-01/scalars/string)· The end time for the availability

[`is_repeating` ](#field-is-repeating)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the availability is repeating

[`range_end` ](#field-range-end)· [`String` ](/reference/2026-01-01/scalars/string)· The end of the availability range

[`range_start` ](#field-range-start)· [`String` ](/reference/2026-01-01/scalars/string)· The start of the availability range

[`time` ](#field-time)· [`String` ](/reference/2026-01-01/scalars/string)· The time for the availability

[`timezone` ](#field-timezone)· [`String` ](/reference/2026-01-01/scalars/string)· The timezone for the availability

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user

## Used By

[`bulkCreateAvailabilityInput.availabilities`](/reference/2026-01-01/input-objects/bulkcreateavailabilityinput)

## Definition

```
"""
Payload for an availability
"""
input AvailabilityInput {
  """
  The ID of the appointment location
  """
  appointment_location_id: String


  """
  The ID of the appointment type
  """
  appointment_type_id: String


  """
  The ID of the contact type
  """
  contact_type_id: String


  """
  The day of the week for the availability
  """
  day_of_week: Int


  """
  The end time for the availability
  """
  end_time: String


  """
  Whether the availability is repeating
  """
  is_repeating: Boolean


  """
  The end of the availability range
  """
  range_end: String


  """
  The start of the availability range
  """
  range_start: String


  """
  The time for the availability
  """
  time: String


  """
  The timezone for the availability
  """
  timezone: String


  """
  The ID of the user
  """
  user_id: String
}
```
