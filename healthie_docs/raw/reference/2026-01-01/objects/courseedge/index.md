---
title: CourseEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/courseedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/courseedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Course` ](/reference/2026-01-01/objects/course)· The item at the end of the edge.

## Used By

[`CoursePaginationConnection.edges`](/reference/2026-01-01/objects/coursepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CourseEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Course
}
```
