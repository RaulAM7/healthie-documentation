---
title: AppointmentPerDayData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentperdaydata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentperdaydata/index.md
---

The appointment count for the specific day

## Fields

[`count` ](#field-count)· [`AppointmentFrequencyDataType` ](/reference/2026-01-01/objects/appointmentfrequencydatatype)· The object with the total count of appointments for each status

[`date` ](#field-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The day we count appointments for

## Used By

[`AppointmentPerTypePerDayData.appointments`](/reference/2026-01-01/objects/appointmentpertypeperdaydata)

[`AppointmentPerUserData.appointments`](/reference/2026-01-01/objects/appointmentperuserdata)

[`AppointmentSummaryData.appointment_history`](/reference/2026-01-01/objects/appointmentsummarydata)

## Definition

```
"""
The appointment count for the specific day
"""
type AppointmentPerDayData {
  """
  The object with the total count of appointments for each status
  """
  count: AppointmentFrequencyDataType


  """
  The day we count appointments for
  """
  date: ISO8601DateTime
}
```
