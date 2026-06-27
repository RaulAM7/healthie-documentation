---
title: AppointmentWorkflowStatusChartNoteType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatuschartnotetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatuschartnotetype/index.md
---

The chart note object for the appointment

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the chart note for the appointment

[`status` ](#field-status)· [`AppointmentWorkflowChartNoteStatus` ](/reference/2026-01-01/enums/appointmentworkflowchartnotestatus)· Status of the chart note for the appointment

[`title` ](#field-title)· [`String` ](/reference/2026-01-01/scalars/string)· The chart note title for the appointment

## Used By

[`AppointmentWorkflowStatus.chart_notes`](/reference/2026-01-01/objects/appointmentworkflowstatus)

## Definition

```
"""
The chart note object for the appointment
"""
type AppointmentWorkflowStatusChartNoteType {
  """
  ID of the chart note for the appointment
  """
  id: ID


  """
  Status of the chart note for the appointment
  """
  status: AppointmentWorkflowChartNoteStatus


  """
  The chart note title for the appointment
  """
  title: String
}
```
