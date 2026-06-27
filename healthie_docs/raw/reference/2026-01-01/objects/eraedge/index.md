---
title: EraEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/eraedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/eraedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Era` ](/reference/2026-01-01/objects/era)· The item at the end of the edge.

## Used By

[`EraConnection.edges`](/reference/2026-01-01/objects/eraconnection)

## Definition

```
"""
An edge in a connection.
"""
type EraEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Era
}
```
