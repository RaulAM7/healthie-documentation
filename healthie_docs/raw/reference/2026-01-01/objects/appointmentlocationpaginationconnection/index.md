---
title: AppointmentLocationPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentlocationpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentlocationpaginationconnection/index.md
---

The connection type for AppointmentLocation.

## Fields

[`edges` ](#field-edges)· [`[AppointmentLocationEdge]` ](/reference/2026-01-01/objects/appointmentlocationedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AppointmentLocation]` ](/reference/2026-01-01/objects/appointmentlocation)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.appointmentLocations`](/reference/2026-01-01/queries/appointmentlocations)

[`Query.providerAppointmentLocations`](/reference/2026-01-01/queries/providerappointmentlocations)

## Definition

```
"""
The connection type for AppointmentLocation.
"""
type AppointmentLocationPaginationConnection {
  """
  A list of edges.
  """
  edges: [AppointmentLocationEdge]


  """
  A list of nodes.
  """
  nodes: [AppointmentLocation]


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
