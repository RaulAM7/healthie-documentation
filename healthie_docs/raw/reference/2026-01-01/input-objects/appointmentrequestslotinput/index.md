---
title: AppointmentRequestSlotInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentrequestslotinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentrequestslotinput/index.md
---

Payload for a time slot for an appointment request

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the appointment request slot

[`slot_start` ](#field-slot-start)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The start time of the requested appointment availability

[`slot_end` ](#field-slot-end)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The end time of the requested appointment availability

## Used By

[`createAppointmentRequestInput.slots`](/reference/2026-01-01/input-objects/createappointmentrequestinput)

## Definition

```
"""
Payload for a time slot for an appointment request
"""
input AppointmentRequestSlotInput {
  """
  The unique identifier of the appointment request slot
  """
  id: ID


  """
  The start time of the requested appointment availability
  """
  slot_start: ISO8601DateTime!


  """
  The end time of the requested appointment availability
  """
  slot_end: ISO8601DateTime!
}
```
