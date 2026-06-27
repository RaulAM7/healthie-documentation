---
title: CptCodeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CptCode` ](/reference/2026-01-01/objects/cptcode)· The item at the end of the edge.

## Used By

[`CptCodePaginationConnection.edges`](/reference/2026-01-01/objects/cptcodepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CptCodeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CptCode
}
```
