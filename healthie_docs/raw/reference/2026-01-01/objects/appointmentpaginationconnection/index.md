---
title: AppointmentPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentpaginationconnection/index.md
---

The connection type for Appointment.

## Fields

[`edges` ](#field-edges)· [`[AppointmentEdge]` ](/reference/2026-01-01/objects/appointmentedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Appointment]` ](/reference/2026-01-01/objects/appointment)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.appointments`](/reference/2026-01-01/queries/appointments)

[`RecurringAppointment.appointments`](/reference/2026-01-01/objects/recurringappointment)

## Definition

```
"""
The connection type for Appointment.
"""
type AppointmentPaginationConnection {
  """
  A list of edges.
  """
  edges: [AppointmentEdge]


  """
  A list of nodes.
  """
  nodes: [Appointment]


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
