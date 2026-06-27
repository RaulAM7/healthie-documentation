---
title: CarePlanEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CarePlan` ](/reference/2026-01-01/objects/careplan)· The item at the end of the edge.

## Used By

[`CarePlanPaginationConnection.edges`](/reference/2026-01-01/objects/careplanpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CarePlanEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CarePlan
}
```
