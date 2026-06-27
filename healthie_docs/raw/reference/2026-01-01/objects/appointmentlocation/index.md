---
title: AppointmentLocation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentlocation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentlocation/index.md
---

A location where appointments are held

## Fields

[`appointment_setting_id` ](#field-appointment-setting-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the associated appointment setting

[`clients_can_book` ](#field-clients-can-book)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Whether the client can select this location or not

[`has_rooms` ](#field-has-rooms)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether the location has any rooms

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the appointment

[`location` ](#field-location)· [`String` ](/reference/2026-01-01/scalars/string)· The location (in plain text)

[`rooms` ](#field-rooms)· [`[Room!]` ](/reference/2026-01-01/objects/room)· The rooms at the location

## Used By

[`AppointmentLocationEdge.node`](/reference/2026-01-01/objects/appointmentlocationedge)

[`AppointmentLocationPaginationConnection.nodes`](/reference/2026-01-01/objects/appointmentlocationpaginationconnection)

[`AppointmentRequestType.appointment_location`](/reference/2026-01-01/objects/appointmentrequesttype)

[`AppointmentSetting.appointment_locations`](/reference/2026-01-01/objects/appointmentsetting)

[`Organization.appointment_locations`](/reference/2026-01-01/objects/organization)

[`User.appointment_locations`](/reference/2026-01-01/objects/user)

[`Query.appointmentLocation`](/reference/2026-01-01/queries/appointmentlocation)

## Definition

```
"""
A location where appointments are held
"""
type AppointmentLocation {
  """
  The ID of the associated appointment setting
  """
  appointment_setting_id: ID


  """
  Whether the client can select this location or not
  """
  clients_can_book: Boolean!


  """
  Whether the location has any rooms
  """
  has_rooms: Boolean


  """
  The unique identifier of the appointment
  """
  id: ID!


  """
  The location (in plain text)
  """
  location: String


  """
  The rooms at the location
  """
  rooms: [Room!]
}
```
