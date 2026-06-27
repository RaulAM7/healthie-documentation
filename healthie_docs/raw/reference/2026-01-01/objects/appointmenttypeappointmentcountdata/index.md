---
title: AppointmentTypeAppointmentCountData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypeappointmentcountdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypeappointmentcountdata/index.md
---

The count of appointments for each appointment type

## Fields

[`appointment_count` ](#field-appointment-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The unique identifier of the count

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the appointment type for which we count appointments for

## Used By

[`AppointmentSummaryData.appointments_per_type_count`](/reference/2026-01-01/objects/appointmentsummarydata)

## Definition

```
"""
The count of appointments for each appointment type
"""
type AppointmentTypeAppointmentCountData {
  """
  The unique identifier of the count
  """
  appointment_count: Int


  """
  The name of the appointment type for which we count appointments for
  """
  name: String
}
```
