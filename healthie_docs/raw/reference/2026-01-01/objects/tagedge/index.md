---
title: TagEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/tagedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/tagedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Tag` ](/reference/2026-01-01/objects/tag)· The item at the end of the edge.

## Used By

[`TagPaginationConnection.edges`](/reference/2026-01-01/objects/tagpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type TagEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Tag
}
```
