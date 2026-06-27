---
title: AppointmentWorkflowStatusAppointmentType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusappointmenttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusappointmenttype/index.md
---

The appointment object

## Fields

[`appointment_category` ](#field-appointment-category)· [`String` ](/reference/2026-01-01/scalars/string)· Category of the appointment: expected values are "Individual" and "Group"

[`date` ](#field-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date of the appointment

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the appointment

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Status of the appointment

## Used By

[`AppointmentWorkflowStatus.appointment`](/reference/2026-01-01/objects/appointmentworkflowstatus)

## Definition

```
"""
The appointment object
"""
type AppointmentWorkflowStatusAppointmentType {
  """
  Category of the appointment: expected values are "Individual" and "Group"
  """
  appointment_category: String


  """
  Date of the appointment
  """
  date: ISO8601DateTime


  """
  ID of the appointment
  """
  id: ID


  """
  Status of the appointment
  """
  status: String
}
```
