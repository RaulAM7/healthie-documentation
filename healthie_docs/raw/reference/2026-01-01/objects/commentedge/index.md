---
title: CommentEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/commentedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/commentedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Comment` ](/reference/2026-01-01/objects/comment)· The item at the end of the edge.

## Used By

[`CommentPaginationConnection.edges`](/reference/2026-01-01/objects/commentpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CommentEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Comment
}
```
