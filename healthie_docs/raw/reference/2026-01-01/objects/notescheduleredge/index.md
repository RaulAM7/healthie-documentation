---
title: NoteSchedulerEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/notescheduleredge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/notescheduleredge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`NoteScheduler` ](/reference/2026-01-01/objects/notescheduler)· The item at the end of the edge.

## Used By

[`NoteSchedulerPaginationConnection.edges`](/reference/2026-01-01/objects/noteschedulerpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type NoteSchedulerEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: NoteScheduler
}
```
