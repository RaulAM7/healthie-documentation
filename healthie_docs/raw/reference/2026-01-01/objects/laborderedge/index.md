---
title: LabOrderEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/laborderedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/laborderedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`LabOrder` ](/reference/2026-01-01/objects/laborder)· The item at the end of the edge.

## Used By

[`LabOrderPaginationConnection.edges`](/reference/2026-01-01/objects/laborderpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type LabOrderEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: LabOrder
}
```
