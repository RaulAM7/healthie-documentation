---
title: CoursePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursepaginationconnection/index.md
---

The connection type for Course.

## Fields

[`edges` ](#field-edges)· [`[CourseEdge]` ](/reference/2026-01-01/objects/courseedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Course]` ](/reference/2026-01-01/objects/course)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.courses`](/reference/2026-01-01/queries/courses)

## Definition

```
"""
The connection type for Course.
"""
type CoursePaginationConnection {
  """
  A list of edges.
  """
  edges: [CourseEdge]


  """
  A list of nodes.
  """
  nodes: [Course]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
