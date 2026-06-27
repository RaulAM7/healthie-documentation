---
title: EntryEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/entryedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/entryedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Entry` ](/reference/2026-01-01/objects/entry)· The item at the end of the edge.

## Used By

[`EntryPaginationConnection.edges`](/reference/2026-01-01/objects/entrypaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type EntryEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Entry
}
```
