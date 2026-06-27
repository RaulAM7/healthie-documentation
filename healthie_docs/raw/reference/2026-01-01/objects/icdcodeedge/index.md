---
title: IcdCodeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`IcdCode` ](/reference/2026-01-01/objects/icdcode)· The item at the end of the edge.

## Used By

[`IcdCodePaginationConnection.edges`](/reference/2026-01-01/objects/icdcodepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type IcdCodeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: IcdCode
}
```
