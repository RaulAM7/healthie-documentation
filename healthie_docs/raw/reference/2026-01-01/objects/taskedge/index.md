---
title: TaskEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/taskedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/taskedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Task` ](/reference/2026-01-01/objects/task)· The item at the end of the edge.

## Used By

[`TaskPaginationConnection.edges`](/reference/2026-01-01/objects/taskpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type TaskEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Task
}
```
