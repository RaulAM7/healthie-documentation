---
title: AppointmentWorkflowStatusProviderType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusprovidertype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusprovidertype/index.md
---

The provider object for the appointment

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the provider for the appointment

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· Name of the provider for the appointment

## Used By

[`AppointmentWorkflowStatus.provider`](/reference/2026-01-01/objects/appointmentworkflowstatus)

## Definition

```
"""
The provider object for the appointment
"""
type AppointmentWorkflowStatusProviderType {
  """
  ID of the provider for the appointment
  """
  id: ID


  """
  Name of the provider for the appointment
  """
  name: String
}
```
