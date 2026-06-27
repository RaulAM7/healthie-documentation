---
title: Cms1500Edge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500edge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500edge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Cms1500` ](/reference/2026-01-01/objects/cms1500)· The item at the end of the edge.

## Used By

[`Cms1500PaginationConnection.edges`](/reference/2026-01-01/objects/cms1500paginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type Cms1500Edge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Cms1500
}
```
