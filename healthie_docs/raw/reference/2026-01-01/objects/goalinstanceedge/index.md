---
title: GoalInstanceEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goalinstanceedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goalinstanceedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`GoalInstance` ](/reference/2026-01-01/objects/goalinstance)· The item at the end of the edge.

## Used By

[`GoalInstancePaginationConnection.edges`](/reference/2026-01-01/objects/goalinstancepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type GoalInstanceEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: GoalInstance
}
```
