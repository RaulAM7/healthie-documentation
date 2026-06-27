---
title: GoalEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goaledge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goaledge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Goal` ](/reference/2026-01-01/objects/goal)· The item at the end of the edge.

## Used By

[`GoalPaginationConnection.edges`](/reference/2026-01-01/objects/goalpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type GoalEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Goal
}
```
