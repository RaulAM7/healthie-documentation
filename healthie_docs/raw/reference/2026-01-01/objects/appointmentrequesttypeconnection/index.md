---
title: AppointmentRequestTypeConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequesttypeconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequesttypeconnection/index.md
---

The connection type for AppointmentRequestType.

## Fields

[`edges` ](#field-edges)· [`[AppointmentRequestTypeEdge]` ](/reference/2026-01-01/objects/appointmentrequesttypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AppointmentRequestType]` ](/reference/2026-01-01/objects/appointmentrequesttype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.appointmentRequests`](/reference/2026-01-01/queries/appointmentrequests)

## Definition

```
"""
The connection type for AppointmentRequestType.
"""
type AppointmentRequestTypeConnection {
  """
  A list of edges.
  """
  edges: [AppointmentRequestTypeEdge]


  """
  A list of nodes.
  """
  nodes: [AppointmentRequestType]


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
