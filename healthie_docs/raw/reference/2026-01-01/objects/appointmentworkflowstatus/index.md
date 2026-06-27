---
title: AppointmentWorkflowStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatus/index.md
---

AppointmentWorkflowStatusType object

## Fields

[`appointment` ](#field-appointment)· [`AppointmentWorkflowStatusAppointmentType` ](/reference/2026-01-01/objects/appointmentworkflowstatusappointmenttype)· Appointment object

[`chart_notes` ](#field-chart-notes)· [`[AppointmentWorkflowStatusChartNoteType!]` ](/reference/2026-01-01/objects/appointmentworkflowstatuschartnotetype)· Chart notes for the appointment

[`chart_notes_count` ](#field-chart-notes-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Total chart notes for the appointment

[`client` ](#field-client)· [`AppointmentWorkflowStatusClientType` ](/reference/2026-01-01/objects/appointmentworkflowstatusclienttype)· The client for the appointment

[`cms1500` ](#field-cms1500)· [`AppointmentWorkflowStatusCms1500Type` ](/reference/2026-01-01/objects/appointmentworkflowstatuscms1500type)· The CMS1500 for the appointment

[`invoice` ](#field-invoice)· [`AppointmentWorkflowStatusInvoiceType` ](/reference/2026-01-01/objects/appointmentworkflowstatusinvoicetype)· The invoice for the appointment

[`provider` ](#field-provider)· [`AppointmentWorkflowStatusProviderType` ](/reference/2026-01-01/objects/appointmentworkflowstatusprovidertype)· The provider for the appointment

## Used By

[`AppointmentWorkflowStatusConnection.nodes`](/reference/2026-01-01/objects/appointmentworkflowstatusconnection)

[`AppointmentWorkflowStatusEdge.node`](/reference/2026-01-01/objects/appointmentworkflowstatusedge)

## Definition

```
"""
AppointmentWorkflowStatusType object
"""
type AppointmentWorkflowStatus {
  """
  Appointment object
  """
  appointment: AppointmentWorkflowStatusAppointmentType


  """
  Chart notes for the appointment
  """
  chart_notes: [AppointmentWorkflowStatusChartNoteType!]


  """
  Total chart notes for the appointment
  """
  chart_notes_count: Int


  """
  The client for the appointment
  """
  client: AppointmentWorkflowStatusClientType


  """
  The CMS1500 for the appointment
  """
  cms1500: AppointmentWorkflowStatusCms1500Type


  """
  The invoice for the appointment
  """
  invoice: AppointmentWorkflowStatusInvoiceType


  """
  The provider for the appointment
  """
  provider: AppointmentWorkflowStatusProviderType
}
```
