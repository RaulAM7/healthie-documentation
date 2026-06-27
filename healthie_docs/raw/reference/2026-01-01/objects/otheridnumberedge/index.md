---
title: OtherIdNumberEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/otheridnumberedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/otheridnumberedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OtherIdNumber` ](/reference/2026-01-01/objects/otheridnumber)· The item at the end of the edge.

## Used By

[`OtherIdNumberPaginationConnection.edges`](/reference/2026-01-01/objects/otheridnumberpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OtherIdNumberEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OtherIdNumber
}
```
