---
title: AppointmentOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentorderkeys/index.md
---

Appointment sorting enum

## Used By

[`Query.appointments`](/reference/2026-01-01/queries/appointments)

[`RecurringAppointment.appointments`](/reference/2026-01-01/objects/recurringappointment)

## Definition

```
"""
Appointment sorting enum
"""
enum AppointmentOrderKeys {
  DATE_ASC
  DATE_DESC
  CREATED_AT_DESC
  CREATED_AT_ASC
  UPDATED_AT_DESC
  UPDATED_AT_ASC
  UNSORTED
}
```
