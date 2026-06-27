---
title: PlaceOfServiceEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/placeofserviceedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/placeofserviceedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`PlaceOfService` ](/reference/2026-01-01/objects/placeofservice)· The item at the end of the edge.

## Used By

[`PlaceOfServicePaginationConnection.edges`](/reference/2026-01-01/objects/placeofservicepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type PlaceOfServiceEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: PlaceOfService
}
```
