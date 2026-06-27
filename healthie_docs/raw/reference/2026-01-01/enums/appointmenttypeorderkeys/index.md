---
title: AppointmentTypeOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmenttypeorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmenttypeorderkeys/index.md
---

Appointment Type sorting enum

## Used By

[`Query.appointmentTypes`](/reference/2026-01-01/queries/appointmenttypes)

## Definition

```
"""
Appointment Type sorting enum
"""
enum AppointmentTypeOrderKeys {
  """
  Sort ascending by the manual order set for Appointment Types on the list
  """
  POSITION_ASC


  """
  Sort descending by the manual order set for Appointment Types on the list
  """
  POSITION_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
}
```
