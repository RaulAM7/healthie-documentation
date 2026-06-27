---
title: RoomInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/roominput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/roominput/index.md
---

Payload for a Room

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the room will be deleted

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the room

[`limit_to_one` ](#field-limit-to-one)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, only one user can be in the room at a time

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the room

## Used By

[`AppointmentLocationInput.rooms`](/reference/2026-01-01/input-objects/appointmentlocationinput)

## Definition

```
"""
Payload for a Room
"""
input RoomInput {
  """
  If true, the room will be deleted
  """
  _destroy: Boolean


  """
  The ID of the room
  """
  id: ID


  """
  If true, only one user can be in the room at a time
  """
  limit_to_one: Boolean


  """
  The graphql_name of the room
  """
  name: String
}
```
