---
title: GoalHistoryPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goalhistorypaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goalhistorypaginationconnection/index.md
---

The connection type for GoalHistory.

## Fields

[`edges` ](#field-edges)· [`[GoalHistoryEdge]` ](/reference/2026-01-01/objects/goalhistoryedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[GoalHistory]` ](/reference/2026-01-01/objects/goalhistory)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.goalHistories`](/reference/2026-01-01/queries/goalhistories)

## Definition

```
"""
The connection type for GoalHistory.
"""
type GoalHistoryPaginationConnection {
  """
  A list of edges.
  """
  edges: [GoalHistoryEdge]


  """
  A list of nodes.
  """
  nodes: [GoalHistory]


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
