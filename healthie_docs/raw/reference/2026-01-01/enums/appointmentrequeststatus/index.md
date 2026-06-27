---
title: AppointmentRequestStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentrequeststatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentrequeststatus/index.md
---

The status of an appointment request

## Used By

[`AppointmentRequestType.current_status`](/reference/2026-01-01/objects/appointmentrequesttype)

[`Query.appointmentRequests`](/reference/2026-01-01/queries/appointmentrequests)

[`Query.appointmentRequests`](/reference/2026-01-01/queries/appointmentrequests)

[`updateAppointmentRequestInput.status`](/reference/2026-01-01/input-objects/updateappointmentrequestinput)

## Definition

```
"""
The status of an appointment request
"""
enum AppointmentRequestStatus {
  """
  Request is active and available for booking appointments
  """
  OPEN


  """
  Request has been closed and is no longer active
  """
  CLOSED
}
```
