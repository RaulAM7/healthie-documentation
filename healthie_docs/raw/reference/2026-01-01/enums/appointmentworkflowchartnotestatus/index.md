---
title: AppointmentWorkflowChartNoteStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentworkflowchartnotestatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/appointmentworkflowchartnotestatus/index.md
---

Chart note statuses

## Used By

[`AppointmentWorkflowStatusChartNoteType.status`](/reference/2026-01-01/objects/appointmentworkflowstatuschartnotetype)

[`Query.appointmentWorkflowStatuses`](/reference/2026-01-01/queries/appointmentworkflowstatuses)

## Definition

```
"""
Chart note statuses
"""
enum AppointmentWorkflowChartNoteStatus {
  CREATED
  SIGNED
  LOCKED
  SIGNED_AND_LOCKED
}
```
