---
title: AutoTaskGeneratorEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/autotaskgeneratoredge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/autotaskgeneratoredge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AutoTaskGenerator` ](/reference/2026-01-01/objects/autotaskgenerator)· The item at the end of the edge.

## Used By

[`AutoTaskGeneratorPaginationConnection.edges`](/reference/2026-01-01/objects/autotaskgeneratorpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AutoTaskGeneratorEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AutoTaskGenerator
}
```
