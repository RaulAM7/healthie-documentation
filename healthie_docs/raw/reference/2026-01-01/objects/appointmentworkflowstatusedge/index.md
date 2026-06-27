---
title: AppointmentWorkflowStatusEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentworkflowstatusedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AppointmentWorkflowStatus` ](/reference/2026-01-01/objects/appointmentworkflowstatus)· The item at the end of the edge.

## Used By

[`AppointmentWorkflowStatusConnection.edges`](/reference/2026-01-01/objects/appointmentworkflowstatusconnection)

## Definition

```
"""
An edge in a connection.
"""
type AppointmentWorkflowStatusEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AppointmentWorkflowStatus
}
```
