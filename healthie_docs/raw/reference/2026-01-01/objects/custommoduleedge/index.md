---
title: CustomModuleEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CustomModule` ](/reference/2026-01-01/objects/custommodule)· The item at the end of the edge.

## Used By

[`CustomModulePaginationConnection.edges`](/reference/2026-01-01/objects/custommodulepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CustomModuleEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CustomModule
}
```
