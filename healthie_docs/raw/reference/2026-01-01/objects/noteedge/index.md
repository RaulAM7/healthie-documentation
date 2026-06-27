---
title: NoteEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/noteedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/noteedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Note` ](/reference/2026-01-01/objects/note)· The item at the end of the edge.

## Used By

[`NotePaginationConnection.edges`](/reference/2026-01-01/objects/notepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type NoteEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Note
}
```
