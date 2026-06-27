---
title: AppointmentWorkflowStatusInvoiceType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusinvoicetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusinvoicetype/index.md
---

The invoice object for the appointment

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the invoice for the appointment

[`status` ](#field-status)· [`String` ](/reference/2026-01-01/scalars/string)· Status of the invoice for the appointment

## Used By

[`AppointmentWorkflowStatus.invoice`](/reference/2026-01-01/objects/appointmentworkflowstatus)

## Definition

```
"""
The invoice object for the appointment
"""
type AppointmentWorkflowStatusInvoiceType {
  """
  ID of the invoice for the appointment
  """
  id: ID


  """
  Status of the invoice for the appointment
  """
  status: String
}
```
