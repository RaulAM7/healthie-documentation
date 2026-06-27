---
title: LabOrderPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/laborderpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/laborderpaginationconnection/index.md
---

The connection type for LabOrder.

## Fields

[`edges` ](#field-edges)· [`[LabOrderEdge]` ](/reference/2026-01-01/objects/laborderedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[LabOrder]` ](/reference/2026-01-01/objects/laborder)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.labOrders`](/reference/2026-01-01/queries/laborders)

## Definition

```
"""
The connection type for LabOrder.
"""
type LabOrderPaginationConnection {
  """
  A list of edges.
  """
  edges: [LabOrderEdge]


  """
  A list of nodes.
  """
  nodes: [LabOrder]


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
