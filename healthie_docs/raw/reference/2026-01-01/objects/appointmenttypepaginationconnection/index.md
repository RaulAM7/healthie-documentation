---
title: AppointmentTypePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypepaginationconnection/index.md
---

The connection type for AppointmentType.

## Fields

[`edges` ](#field-edges)· [`[AppointmentTypeEdge]` ](/reference/2026-01-01/objects/appointmenttypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AppointmentType]` ](/reference/2026-01-01/objects/appointmenttype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.appointmentTypes`](/reference/2026-01-01/queries/appointmenttypes)

## Definition

```
"""
The connection type for AppointmentType.
"""
type AppointmentTypePaginationConnection {
  """
  A list of edges.
  """
  edges: [AppointmentTypeEdge]


  """
  A list of nodes.
  """
  nodes: [AppointmentType]


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
