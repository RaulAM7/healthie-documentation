---
title: AppointmentFrequencyDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentfrequencydatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentfrequencydatatype/index.md
---

Appointment Frequency Data

## Fields

[`cancelled` ](#field-cancelled)· [`Int` ](/reference/2026-01-01/scalars/int)· Frequency of cancelled appointments

[`checked_in` ](#field-checked-in)· [`Int` ](/reference/2026-01-01/scalars/int)· Frequency of checked-in appointments

[`late_cancellation` ](#field-late-cancellation)· [`Int` ](/reference/2026-01-01/scalars/int)· Frequency of late cancellation appointments

[`no_status` ](#field-no-status)· [`Int` ](/reference/2026-01-01/scalars/int)· Frequency of appointments with no status

[`noshow` ](#field-noshow)· [`Int` ](/reference/2026-01-01/scalars/int)· Frequency of no-show appointments

[`occurred` ](#field-occurred)· [`Int` ](/reference/2026-01-01/scalars/int)· Frequency of occurred appointments

[`rescheduled` ](#field-rescheduled)· [`Int` ](/reference/2026-01-01/scalars/int)· Frequency of rescheduled appointments

## Used By

[`AppointmentDataType.freq`](/reference/2026-01-01/objects/appointmentdatatype)

[`AppointmentPerDayData.count`](/reference/2026-01-01/objects/appointmentperdaydata)

## Definition

```
"""
Appointment Frequency Data
"""
type AppointmentFrequencyDataType {
  """
  Frequency of cancelled appointments
  """
  cancelled: Int


  """
  Frequency of checked-in appointments
  """
  checked_in: Int


  """
  Frequency of late cancellation appointments
  """
  late_cancellation: Int


  """
  Frequency of appointments with no status
  """
  no_status: Int


  """
  Frequency of no-show appointments
  """
  noshow: Int


  """
  Frequency of occurred appointments
  """
  occurred: Int


  """
  Frequency of rescheduled appointments
  """
  rescheduled: Int
}
```
