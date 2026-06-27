---
title: Room | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/room/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/room/index.md
---

A room at a location

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique ID for this room

[`limit_to_one` ](#field-limit-to-one)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · When true, there can only be one appointment at a time in the room

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the room

## Used By

[`AppointmentLocation.rooms`](/reference/2026-01-01/objects/appointmentlocation)

## Definition

```
"""
A room at a location
"""
type Room {
  """
  Unique ID for this room
  """
  id: ID!


  """
  When true, there can only be one appointment at a time in the room
  """
  limit_to_one: Boolean!


  """
  Name of the room
  """
  name: String
}
```
