---
title: CourseItemEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/courseitemedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/courseitemedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CourseItem` ](/reference/2026-01-01/objects/courseitem)· The item at the end of the edge.

## Used By

[`CourseItemPaginationConnection.edges`](/reference/2026-01-01/objects/courseitempaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CourseItemEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CourseItem
}
```
