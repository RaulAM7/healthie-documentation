---
title: DocumentViewingEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/documentviewingedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/documentviewingedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`DocumentViewing` ](/reference/2026-01-01/objects/documentviewing)· The item at the end of the edge.

## Used By

[`DocumentViewingPaginationConnection.edges`](/reference/2026-01-01/objects/documentviewingpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type DocumentViewingEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: DocumentViewing
}
```
