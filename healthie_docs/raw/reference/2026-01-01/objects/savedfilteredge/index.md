---
title: SavedFilterEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/savedfilteredge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/savedfilteredge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`SavedFilter` ](/reference/2026-01-01/objects/savedfilter)· The item at the end of the edge.

## Used By

[`SavedFilterPaginationConnection.edges`](/reference/2026-01-01/objects/savedfilterpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type SavedFilterEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: SavedFilter
}
```
