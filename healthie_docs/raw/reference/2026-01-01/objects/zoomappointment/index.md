---
title: ZoomAppointment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/zoomappointment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/zoomappointment/index.md
---

Zoom meeting retrieved from Zoom API

## Fields

[`duration` ](#field-duration)· [`Int` ](/reference/2026-01-01/scalars/int)· The total number of minutes attended by the meeting's host and participants

[`end_time` ](#field-end-time)· [`String` ](/reference/2026-01-01/scalars/string)· End time of meeting

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The unique identifier of the zoom appointment

[`participants_count` ](#field-participants-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of meeting participants

[`start_time` ](#field-start-time)· [`String` ](/reference/2026-01-01/scalars/string)· Start time of meeting

[`total_minutes` ](#field-total-minutes)· [`Int` ](/reference/2026-01-01/scalars/int)· The meeting's duration, in minutes

## Used By

[`Appointment.zoom_appointment`](/reference/2026-01-01/objects/appointment)

## Definition

```
"""
Zoom meeting retrieved from Zoom API
"""
type ZoomAppointment {
  """
  The total number of minutes attended by the meeting's host and participants
  """
  duration: Int


  """
  End time of meeting
  """
  end_time: String


  """
  The unique identifier of the zoom appointment
  """
  id: ID


  """
  The number of meeting participants
  """
  participants_count: Int


  """
  Start time of meeting
  """
  start_time: String


  """
  The meeting's duration, in minutes
  """
  total_minutes: Int
}
```
