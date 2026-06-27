---
title: GoalPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goalpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goalpaginationconnection/index.md
---

The connection type for Goal.

## Fields

[`edges` ](#field-edges)· [`[GoalEdge]` ](/reference/2026-01-01/objects/goaledge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Goal]` ](/reference/2026-01-01/objects/goal)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.goals`](/reference/2026-01-01/queries/goals)

[`Query.subGoals`](/reference/2026-01-01/queries/subgoals)

## Definition

```
"""
The connection type for Goal.
"""
type GoalPaginationConnection {
  """
  A list of edges.
  """
  edges: [GoalEdge]


  """
  A list of nodes.
  """
  nodes: [Goal]


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
