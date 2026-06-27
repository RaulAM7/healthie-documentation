---
title: FolderEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/folderedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/folderedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Folder` ](/reference/2026-01-01/objects/folder)· The item at the end of the edge.

## Used By

[`FolderPaginationConnection.edges`](/reference/2026-01-01/objects/folderpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type FolderEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Folder
}
```
