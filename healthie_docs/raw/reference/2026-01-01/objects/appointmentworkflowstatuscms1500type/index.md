---
title: AppointmentWorkflowStatusCms1500Type | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatuscms1500type/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatuscms1500type/index.md
---

The cms1500 object for the appointment

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the cms1500 for the appointment

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Status of the cms1500 for the appointment

## Used By

[`AppointmentWorkflowStatus.cms1500`](/reference/2026-01-01/objects/appointmentworkflowstatus)

## Definition

```
"""
The cms1500 object for the appointment
"""
type AppointmentWorkflowStatusCms1500Type {
  """
  ID of the cms1500 for the appointment
  """
  id: ID


  """
  Status of the cms1500 for the appointment
  """
  status: String
}
```
