---
title: AppointmentWorkflowStatusClientType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusclienttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusclienttype/index.md
---

The client object for the appointment

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the client for the appointment

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the client for the appointment

## Used By

[`AppointmentWorkflowStatus.client`](/reference/2026-01-01/objects/appointmentworkflowstatus)

## Definition

```
"""
The client object for the appointment
"""
type AppointmentWorkflowStatusClientType {
  """
  ID of the client for the appointment
  """
  id: ID


  """
  Name of the client for the appointment
  """
  name: String
}
```
