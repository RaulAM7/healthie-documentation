---
title: AppointmentPerUserData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentperuserdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentperuserdata/index.md
---

Appointments for each status for the specific day

## Fields

[`appointments` ](#field-appointments)· [`[AppointmentPerDayData!]` ](/reference/2026-01-01/objects/appointmentperdaydata)· The array containing the appointment count for each appointment status for the specific day

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the provider who we count appointments for

## Used By

[`AppointmentSummaryData.appointment_history_per_provider`](/reference/2026-01-01/objects/appointmentsummarydata)

## Definition

```
"""
Appointments for each status for the specific day
"""
type AppointmentPerUserData {
  """
  The array containing the appointment count for each appointment status for the specific day
  """
  appointments: [AppointmentPerDayData!]


  """
  The name of the provider who we count appointments for
  """
  name: String
}
```
