---
title: AppointmentRequestSlotType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequestslottype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequestslottype/index.md
---

An range of time requested for an appointment request

## Fields

[`appointment_request_id` ](#field-appointment-request-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The identifier of the parent appointment request

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the appointment request slot

[`slot_end` ](#field-slot-end)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The end time of the appointment request slot

[`slot_start` ](#field-slot-start)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The start time of the appointment request slot

## Used By

[`AppointmentRequestType.slots`](/reference/2026-01-01/objects/appointmentrequesttype)

## Definition

```
"""
An range of time requested for an appointment request
"""
type AppointmentRequestSlotType {
  """
  The identifier of the parent appointment request
  """
  appointment_request_id: ID!


  """
  The unique identifier of the appointment request slot
  """
  id: ID!


  """
  The end time of the appointment request slot
  """
  slot_end: ISO8601DateTime!


  """
  The start time of the appointment request slot
  """
  slot_start: ISO8601DateTime!
}
```
