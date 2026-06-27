---
title: AppointmentWorkflowStatusConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusconnection/index.md
---

The connection type for AppointmentWorkflowStatus.

## Fields

[`edges` ](#field-edges)· [`[AppointmentWorkflowStatusEdge]` ](/reference/2026-01-01/objects/appointmentworkflowstatusedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AppointmentWorkflowStatus]` ](/reference/2026-01-01/objects/appointmentworkflowstatus)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.appointmentWorkflowStatuses`](/reference/2026-01-01/queries/appointmentworkflowstatuses)

## Definition

```
"""
The connection type for AppointmentWorkflowStatus.
"""
type AppointmentWorkflowStatusConnection {
  """
  A list of edges.
  """
  edges: [AppointmentWorkflowStatusEdge]


  """
  A list of nodes.
  """
  nodes: [AppointmentWorkflowStatus]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
