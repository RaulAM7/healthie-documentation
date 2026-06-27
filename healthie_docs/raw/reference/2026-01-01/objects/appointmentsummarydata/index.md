---
title: AppointmentSummaryData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentsummarydata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentsummarydata/index.md
---

The data for the appointment summary

## Fields

[`appointment_history` ](#field-appointment-history)· [`[AppointmentPerDayData!]` ](/reference/2026-01-01/objects/appointmentperdaydata)· The array containing the appointment count for each appointment status for the specific day

[`appointment_history_per_provider` ](#field-appointment-history-per-provider)· [`[AppointmentPerUserData!]` ](/reference/2026-01-01/objects/appointmentperuserdata)· The array containing the appointment count for each appointment status for each provider for the specific day

[`appointment_history_per_provider_and_type` ](#field-appointment-history-per-provider-and-type)· [`[AppointmentPerTypePerUserData!]` ](/reference/2026-01-01/objects/appointmentpertypeperuserdata)· The array containing the appointment count for each appointment status for each provider for each appointment type for the specific day

[`appointment_history_per_type` ](#field-appointment-history-per-type)· [`[AppointmentPerTypePerDayData!]` ](/reference/2026-01-01/objects/appointmentpertypeperdaydata)· The array containing the appointment count for each appointment status for each appointment type for the specific day

[`appointments_per_type_count` ](#field-appointments-per-type-count)· [`[AppointmentTypeAppointmentCountData!]` ](/reference/2026-01-01/objects/appointmenttypeappointmentcountdata)· The count of appointments for each appointment type

[`avg_per_day` ](#field-avg-per-day)· [`Int` ](/reference/2026-01-01/scalars/int)· The average amount of appointments per day

[`avg_per_day_percent_diff` ](#field-avg-per-day-percent-diff)· [`Int` ](/reference/2026-01-01/scalars/int)· The difference between the current average amount of appointments and the average count of appointments in prior period

[`busiest_days_of_week` ](#field-busiest-days-of-week)· [`[String]` ](/reference/2026-01-01/scalars/string)· The busiest week day in selected period

[`cache_generation_in_progress` ](#field-cache-generation-in-progress)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, the data is in the process of being generated and stored in the cache.

[`percent_diff` ](#field-percent-diff)· [`Int` ](/reference/2026-01-01/scalars/int)· The difference in contrast to previous period in percents

[`total_count` ](#field-total-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The total appointment count

## Used By

[`Query.appointmentsSummary`](/reference/2026-01-01/queries/appointmentssummary)

## Definition

```
"""
The data for the appointment summary
"""
type AppointmentSummaryData {
  """
  The array containing the appointment count for each appointment status for the specific day
  """
  appointment_history: [AppointmentPerDayData!]


  """
  The array containing the appointment count for each appointment status for each provider for the specific day
  """
  appointment_history_per_provider: [AppointmentPerUserData!]


  """
  The array containing the appointment count for each appointment status for each provider for each appointment type for the specific day
  """
  appointment_history_per_provider_and_type: [AppointmentPerTypePerUserData!]


  """
  The array containing the appointment count for each appointment status for each appointment type for the specific day
  """
  appointment_history_per_type: [AppointmentPerTypePerDayData!]


  """
  The count of appointments for each appointment type
  """
  appointments_per_type_count: [AppointmentTypeAppointmentCountData!]


  """
  The average amount of appointments per day
  """
  avg_per_day: Int


  """
  The difference between the current average amount of appointments and the average count of appointments in prior period
  """
  avg_per_day_percent_diff: Int


  """
  The busiest week day in selected period
  """
  busiest_days_of_week: [String]


  """
  When true, the data is in the process of being generated and stored in the cache.
  """
  cache_generation_in_progress: Boolean


  """
  The difference in contrast to previous period in percents
  """
  percent_diff: Int


  """
  The total appointment count
  """
  total_count: Int
}
```
