---
title: AppointmentCreditChangePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentcreditchangepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentcreditchangepaginationconnection/index.md
---

The connection type for AppointmentCreditChange.

## Fields

[`edges` ](#field-edges)· [`[AppointmentCreditChangeEdge]` ](/reference/2026-01-01/objects/appointmentcreditchangeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AppointmentCreditChange]` ](/reference/2026-01-01/objects/appointmentcreditchange)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.appointmentTypeCreditChanges`](/reference/2026-01-01/queries/appointmenttypecreditchanges)

## Definition

```
"""
The connection type for AppointmentCreditChange.
"""
type AppointmentCreditChangePaginationConnection {
  """
  A list of edges.
  """
  edges: [AppointmentCreditChangeEdge]


  """
  A list of nodes.
  """
  nodes: [AppointmentCreditChange]


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
