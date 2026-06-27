---
title: appointmentLocation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentlocation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/appointmentlocation/index.md
---

fetch an appointment location by id (considered public)

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`AppointmentLocation`](/reference/2026-01-01/objects/appointmentlocation)

## Example

```
query appointmentLocation($id: ID) {
  appointmentLocation(id: $id) {
    appointment_setting_id
    clients_can_book
    has_rooms
    id
    location
    rooms
  }
}
```
