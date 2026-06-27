---
title: RequestedPaymentStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/requestedpaymentstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/requestedpaymentstatus/index.md
---

Requested Payment statuses

## Used By

[`Query.appointmentWorkflowStatuses`](/reference/2026-01-01/queries/appointmentworkflowstatuses)

## Definition

```
"""
Requested Payment statuses
"""
enum RequestedPaymentStatus {
  """
  Paid
  """
  PAID


  """
  Not_Yet_Paid
  """
  NOT_YET_PAID


  """
  Partial
  """
  PARTIAL
}
```
