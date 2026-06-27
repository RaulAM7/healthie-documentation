---
title: AppointmentPerTypePerUserData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpertypeperuserdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpertypeperuserdata/index.md
---

The data type for the appointment count for each appointment type per user

## Fields

[`appointment_types` ](#field-appointment-types)· [`[AppointmentPerTypePerDayData!]` ](/reference/2026-01-01/objects/appointmentpertypeperdaydata)· The array containing the appointment count for each appointment type for each appointment status for the specific day

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the specific user who we count appointments for

## Used By

[`AppointmentSummaryData.appointment_history_per_provider_and_type`](/reference/2026-01-01/objects/appointmentsummarydata)

## Definition

```
"""
The data type for the appointment count for each appointment type per user
"""
type AppointmentPerTypePerUserData {
  """
  The array containing the appointment count for each appointment type for each appointment status for the specific day
  """
  appointment_types: [AppointmentPerTypePerDayData!]


  """
  The name of the specific user who we count appointments for
  """
  name: String
}
```
