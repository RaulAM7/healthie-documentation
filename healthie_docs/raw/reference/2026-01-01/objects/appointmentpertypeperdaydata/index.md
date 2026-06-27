---
title: AppointmentPerTypePerDayData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpertypeperdaydata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpertypeperdaydata/index.md
---

Appointments for the specific type and day

## Fields

[`appointments` ](#field-appointments)· [`[AppointmentPerDayData!]` ](/reference/2026-01-01/objects/appointmentperdaydata)· The array containing the appointment count for each appointment status for the specific day

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the specific appointment type

## Used By

[`AppointmentPerTypePerUserData.appointment_types`](/reference/2026-01-01/objects/appointmentpertypeperuserdata)

[`AppointmentSummaryData.appointment_history_per_type`](/reference/2026-01-01/objects/appointmentsummarydata)

## Definition

```
"""
Appointments for the specific type and day
"""
type AppointmentPerTypePerDayData {
  """
  The array containing the appointment count for each appointment status for the specific day
  """
  appointments: [AppointmentPerDayData!]


  """
  The name of the specific appointment type
  """
  name: String
}
```
