---
title: TaskPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/taskpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/taskpaginationconnection/index.md
---

The connection type for Task.

## Fields

[`edges` ](#field-edges)· [`[TaskEdge]` ](/reference/2026-01-01/objects/taskedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Task]` ](/reference/2026-01-01/objects/task)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.tasks`](/reference/2026-01-01/queries/tasks)

## Definition

```
"""
The connection type for Task.
"""
type TaskPaginationConnection {
  """
  A list of edges.
  """
  edges: [TaskEdge]


  """
  A list of nodes.
  """
  nodes: [Task]


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
