---
title: FoodPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/foodpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/foodpaginationconnection/index.md
---

The connection type for Food.

## Fields

[`edges` ](#field-edges)· [`[FoodEdge]` ](/reference/2026-01-01/objects/foodedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Food]` ](/reference/2026-01-01/objects/food)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.foodSearch`](/reference/2026-01-01/queries/foodsearch)

## Definition

```
"""
The connection type for Food.
"""
type FoodPaginationConnection {
  """
  A list of edges.
  """
  edges: [FoodEdge]


  """
  A list of nodes.
  """
  nodes: [Food]


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
