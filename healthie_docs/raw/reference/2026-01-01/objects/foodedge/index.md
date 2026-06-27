---
title: FoodEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/foodedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/foodedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Food` ](/reference/2026-01-01/objects/food)· The item at the end of the edge.

## Used By

[`FoodPaginationConnection.edges`](/reference/2026-01-01/objects/foodpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type FoodEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Food
}
```
