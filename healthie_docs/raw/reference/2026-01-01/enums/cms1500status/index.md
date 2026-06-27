---
title: Cms1500Status | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/cms1500status/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/cms1500status/index.md
---

Status options for a CMS1500 form

## Used By

[`Cms1500.status`](/reference/2026-01-01/objects/cms1500)

[`Query.appointmentWorkflowStatuses`](/reference/2026-01-01/queries/appointmentworkflowstatuses)

[`Query.cms1500s`](/reference/2026-01-01/queries/cms1500s)

[`updateCms1500Input.status`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Status options for a CMS1500 form
"""
enum Cms1500Status {
  """
  Scheduled
  """
  SCHEDULED


  """
  Sent
  """
  SENT


  """
  Not Sent
  """
  NOT_SENT


  """
  Partially Paid
  """
  PARTIALLY_PAID


  """
  Batched
  """
  BATCHED


  """
  Closed
  """
  CLOSED


  """
  Fully Paid
  """
  FULLY_PAID


  """
  Client's Deductible Applies
  """
  CLIENTS_DEDUCTIBLE_APPLIES


  """
  Rejected by Clearinghouse
  """
  REJECTED


  """
  Denied by Insurance
  """
  DENIED
}
```
