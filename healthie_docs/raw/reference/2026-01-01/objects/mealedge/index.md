---
title: MealEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/mealedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/mealedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Meal` ](/reference/2026-01-01/objects/meal)· The item at the end of the edge.

## Used By

[`MealPaginationConnection.edges`](/reference/2026-01-01/objects/mealpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type MealEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Meal
}
```
