---
title: LocationEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/locationedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/locationedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Location` ](/reference/2026-01-01/objects/location)· The item at the end of the edge.

## Used By

[`LocationPaginationConnection.edges`](/reference/2026-01-01/objects/locationpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type LocationEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Location
}
```
