---
title: EraServiceLineEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/eraservicelineedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/eraservicelineedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`EraServiceLine` ](/reference/2026-01-01/objects/eraserviceline)· The item at the end of the edge.

## Used By

[`EraServiceLineConnection.edges`](/reference/2026-01-01/objects/eraservicelineconnection)

## Definition

```
"""
An edge in a connection.
"""
type EraServiceLineEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: EraServiceLine
}
```
