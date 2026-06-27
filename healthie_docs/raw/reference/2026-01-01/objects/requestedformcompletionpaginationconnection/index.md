---
title: RequestedFormCompletionPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformcompletionpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformcompletionpaginationconnection/index.md
---

The connection type for RequestedFormCompletion.

## Fields

[`edges` ](#field-edges)· [`[RequestedFormCompletionEdge]` ](/reference/2026-01-01/objects/requestedformcompletionedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[RequestedFormCompletion]` ](/reference/2026-01-01/objects/requestedformcompletion)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.requestedFormCompletions`](/reference/2026-01-01/queries/requestedformcompletions)

## Definition

```
"""
The connection type for RequestedFormCompletion.
"""
type RequestedFormCompletionPaginationConnection {
  """
  A list of edges.
  """
  edges: [RequestedFormCompletionEdge]


  """
  A list of nodes.
  """
  nodes: [RequestedFormCompletion]


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
