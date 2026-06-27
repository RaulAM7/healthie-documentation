---
title: DocumentEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/documentedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/documentedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Document` ](/reference/2026-01-01/objects/document)· The item at the end of the edge.

## Used By

[`DocumentPaginationConnection.edges`](/reference/2026-01-01/objects/documentpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type DocumentEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Document
}
```
