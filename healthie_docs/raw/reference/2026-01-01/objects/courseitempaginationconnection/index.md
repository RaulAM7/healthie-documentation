---
title: CourseItemPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/courseitempaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/courseitempaginationconnection/index.md
---

The connection type for CourseItem.

## Fields

[`edges` ](#field-edges)· [`[CourseItemEdge]` ](/reference/2026-01-01/objects/courseitemedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CourseItem]` ](/reference/2026-01-01/objects/courseitem)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.courseItems`](/reference/2026-01-01/queries/courseitems)

## Definition

```
"""
The connection type for CourseItem.
"""
type CourseItemPaginationConnection {
  """
  A list of edges.
  """
  edges: [CourseItemEdge]


  """
  A list of nodes.
  """
  nodes: [CourseItem]


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
