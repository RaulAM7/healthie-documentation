---
title: Availability | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/availability/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/availability/index.md
---

An object containing availability ranges for a provider

## Fields

[`appointment_location_id` ](#field-appointment-location-id)· [`String` ](/reference/2026-01-01/scalars/string)· If not nil, the specific location the availability is for

[`appointment_type_id` ](#field-appointment-type-id)· [`Int` ](/reference/2026-01-01/scalars/int)· If not nil, the specific appointment type the availability is for

[`appointment_types` ](#field-appointment-types)· [`[AppointmentType!]` ](/reference/2026-01-01/objects/appointmenttype)· Appointment types associated with this availability via the many-to-many join

[`contact_type_id` ](#field-contact-type-id)· [`Int` ](/reference/2026-01-01/scalars/int)· If not nil, the specific contact type the availability is for

[`created_at` ](#field-created-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time the availability was created

[`day_of_week` ](#field-day-of-week)· [`Int` ](/reference/2026-01-01/scalars/int)· The 0-indexed day of the week the availability is on

[`duration_string` ](#field-duration-string)· [`String` ](/reference/2026-01-01/scalars/string)· Duration between range start and range end in hours and minutes. Example:(4h 20min)

[`end_on` ](#field-end-on)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The end date of the availability

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the availability (if the availability is repeating, this will be a unique identifier comprised of the date and ID of the availability)

[`is_repeating` ](#field-is-repeating)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The status of whether the availability repeats every week

[`origin_start_date` ](#field-origin-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The origin start of the availability

[`range_end` ](#field-range-end)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The end of the datetime of the availability

[`range_start` ](#field-range-start)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The start of the datetime of the availability

[`repeating_availability_id` ](#field-repeating-availability-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Availability ID if the availability is repeating

[`resourceId` ](#field-resourceid)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user, used for the calendar

[`timezone` ](#field-timezone)· [`String` ](/reference/2026-01-01/scalars/string)· Timezone of the availability passed in when it was created

[`timezone_abbr` ](#field-timezone-abbr)· [`String` ](/reference/2026-01-01/scalars/string)· Timezone abbreviation of the availability time range

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The time the availability was last updated

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Provider this availability belongs to

[`user_id` ](#field-user-id)· [`Int` ](/reference/2026-01-01/scalars/int)· The ID of the person who the availability is for

## Used By

[`CreateAvailabilityWithAppointmentTypesPayload.availability`](/reference/2026-01-01/objects/createavailabilitywithappointmenttypespayload)

[`EditAvailabilityWithAppointmentTypesPayload.availability`](/reference/2026-01-01/objects/editavailabilitywithappointmenttypespayload)

[`bulkCreateAvailabilityPayload.availabilities`](/reference/2026-01-01/objects/bulkcreateavailabilitypayload)

[`createAvailabilityPayload.availability`](/reference/2026-01-01/objects/createavailabilitypayload)

[`deleteAvailabilityPayload.availability`](/reference/2026-01-01/objects/deleteavailabilitypayload)

[`editAvailabilityPayload.availability`](/reference/2026-01-01/objects/editavailabilitypayload)

[`Query.availabilities`](/reference/2026-01-01/queries/availabilities)

[`Query.availability`](/reference/2026-01-01/queries/availability)

## Definition

```
"""
An object containing availability ranges for a provider
"""
type Availability {
  """
  If not nil, the specific location the availability is for
  """
  appointment_location_id: String


  """
  If not nil, the specific appointment type the availability is for
  """
  appointment_type_id: Int


  """
  Appointment types associated with this availability via the many-to-many join
  """
  appointment_types: [AppointmentType!]


  """
  If not nil, the specific contact type the availability is for
  """
  contact_type_id: Int


  """
  The time the availability was created
  """
  created_at: ISO8601DateTime


  """
  The 0-indexed day of the week the availability is on
  """
  day_of_week: Int


  """
  Duration between range start and range end in hours and minutes. Example:(4h 20min)
  """
  duration_string: String


  """
  The end date of the availability
  """
  end_on: ISO8601Date


  """
  The unique identifier of the availability (if the availability is repeating, this will be a unique identifier comprised of the date and ID of the availability)
  """
  id: ID!


  """
  The status of whether the availability repeats every week
  """
  is_repeating: Boolean


  """
  The origin start of the availability
  """
  origin_start_date: ISO8601DateTime


  """
  The end of the datetime of the availability
  """
  range_end: ISO8601DateTime


  """
  The start of the datetime of the availability
  """
  range_start: ISO8601DateTime


  """
  Availability ID if the availability is repeating
  """
  repeating_availability_id: ID


  """
  The ID of the user, used for the calendar
  """
  resourceId: String


  """
  Timezone of the availability passed in when it was created
  """
  timezone: String


  """
  Timezone abbreviation of the availability time range
  """
  timezone_abbr: String


  """
  The time the availability was last updated
  """
  updated_at: ISO8601DateTime


  """
  Provider this availability belongs to
  """
  user: User


  """
  The ID of the person who the availability is for
  """
  user_id: Int
}
```
