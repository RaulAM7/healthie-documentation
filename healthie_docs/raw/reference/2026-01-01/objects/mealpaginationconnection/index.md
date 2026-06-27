---
title: MealPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/mealpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/mealpaginationconnection/index.md
---

The connection type for Meal.

## Fields

[`edges` ](#field-edges)· [`[MealEdge]` ](/reference/2026-01-01/objects/mealedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Meal]` ](/reference/2026-01-01/objects/meal)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.mealSearch`](/reference/2026-01-01/queries/mealsearch)

## Definition

```
"""
The connection type for Meal.
"""
type MealPaginationConnection {
  """
  A list of edges.
  """
  edges: [MealEdge]


  """
  A list of nodes.
  """
  nodes: [Meal]


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
