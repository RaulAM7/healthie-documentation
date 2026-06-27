---
title: LabOptionEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/laboptionedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/laboptionedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`LabOption` ](/reference/2026-01-01/objects/laboption)· The item at the end of the edge.

## Used By

[`LabOptionPaginationConnection.edges`](/reference/2026-01-01/objects/laboptionpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type LabOptionEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: LabOption
}
```
