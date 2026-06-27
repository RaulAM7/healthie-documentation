---
title: NoteSchedulerPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/noteschedulerpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/noteschedulerpaginationconnection/index.md
---

The connection type for NoteScheduler.

## Fields

[`edges` ](#field-edges)· [`[NoteSchedulerEdge]` ](/reference/2026-01-01/objects/notescheduleredge)· A list of edges.

[`nodes` ](#field-nodes)· [`[NoteScheduler]` ](/reference/2026-01-01/objects/notescheduler)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.scheduledMessageBlasts`](/reference/2026-01-01/queries/scheduledmessageblasts)

## Definition

```
"""
The connection type for NoteScheduler.
"""
type NoteSchedulerPaginationConnection {
  """
  A list of edges.
  """
  edges: [NoteSchedulerEdge]


  """
  A list of nodes.
  """
  nodes: [NoteScheduler]


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
