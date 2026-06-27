---
title: appointmentInclusion | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentinclusion/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentinclusion/index.md
---

fetch an appointment by id, group appointments are (considered public)

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`uuid` ](#argument-uuid)· [`ID` ](/reference/2026-01-01/scalars/id)· When external reschedule/cancellation is allowed, the UUID can be used to allow the holder to retrieve and update/cancel their inclusion in an appointment.

## Returns

[`AppointmentInclusionType`](/reference/2026-01-01/objects/appointmentinclusiontype)

## Example

```
query appointmentInclusion($id: ID, $uuid: ID) {
  appointmentInclusion(id: $id, uuid: $uuid) {
    appointment
    attended
    cancellation_reason
    cancelled
    cancelled_at
    cancelled_by
    cancelled_by_id
    confirmed
    external_uuid
    id
    join_time
    leave_time
    other_cancellation_reason
    user
  }
}
```
