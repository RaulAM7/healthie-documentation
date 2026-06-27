---
title: AppointmentLocationInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentlocationinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/appointmentlocationinput/index.md
---

Payload for an appointment location

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the location will be deleted

[`clients_can_book` ](#field-clients-can-book)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, clients can book appointments at this location

[`has_rooms` ](#field-has-rooms)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, this location has rooms

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the location

[`location` ](#field-location)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the location

[`rooms` ](#field-rooms)· [`[RoomInput]` ](/reference/2026-01-01/input-objects/roominput)· The rooms at this location

## Used By

[`createAppointmentSettingInput.appointment_locations`](/reference/2026-01-01/input-objects/createappointmentsettinginput)

[`updateAppointmentSettingInput.appointment_locations`](/reference/2026-01-01/input-objects/updateappointmentsettinginput)

## Definition

```
"""
Payload for an appointment location
"""
input AppointmentLocationInput {
  """
  If true, the location will be deleted
  """
  _destroy: Boolean


  """
  If true, clients can book appointments at this location
  """
  clients_can_book: Boolean


  """
  If true, this location has rooms
  """
  has_rooms: Boolean


  """
  The ID of the location
  """
  id: ID


  """
  The graphql_name of the location
  """
  location: String


  """
  The rooms at this location
  """
  rooms: [RoomInput]
}
```
