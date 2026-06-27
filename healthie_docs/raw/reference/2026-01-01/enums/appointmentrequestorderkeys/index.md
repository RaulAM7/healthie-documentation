---
title: AppointmentRequestOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentrequestorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentrequestorderkeys/index.md
---

Appointment Request sorting enum

## Used By

[`Query.appointmentRequests`](/reference/2026-01-01/queries/appointmentrequests)

## Definition

```
"""
Appointment Request sorting enum
"""
enum AppointmentRequestOrderKeys {
  date_asc
  date_desc
  appt_type
  client_name
  req_provider
  new_clients
  active_clients
  requested_date_asc
  requested_date_desc
}
```
