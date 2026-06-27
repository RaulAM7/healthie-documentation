---
title: CarePlanPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanpaginationconnection/index.md
---

The connection type for CarePlan.

## Fields

[`edges` ](#field-edges)· [`[CarePlanEdge]` ](/reference/2026-01-01/objects/careplanedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CarePlan]` ](/reference/2026-01-01/objects/careplan)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.carePlans`](/reference/2026-01-01/queries/careplans)

## Definition

```
"""
The connection type for CarePlan.
"""
type CarePlanPaginationConnection {
  """
  A list of edges.
  """
  edges: [CarePlanEdge]


  """
  A list of nodes.
  """
  nodes: [CarePlan]


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
