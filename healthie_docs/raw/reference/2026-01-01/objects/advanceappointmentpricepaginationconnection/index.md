---
title: AdvanceAppointmentPricePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/advanceappointmentpricepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/advanceappointmentpricepaginationconnection/index.md
---

The connection type for AdvanceAppointmentPrice.

## Fields

[`edges` ](#field-edges)· [`[AdvanceAppointmentPriceEdge]` ](/reference/2026-01-01/objects/advanceappointmentpriceedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AdvanceAppointmentPrice]` ](/reference/2026-01-01/objects/advanceappointmentprice)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.advanceAppointmentPrices`](/reference/2026-01-01/queries/advanceappointmentprices)

## Definition

```
"""
The connection type for AdvanceAppointmentPrice.
"""
type AdvanceAppointmentPricePaginationConnection {
  """
  A list of edges.
  """
  edges: [AdvanceAppointmentPriceEdge]


  """
  A list of nodes.
  """
  nodes: [AdvanceAppointmentPrice]


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
