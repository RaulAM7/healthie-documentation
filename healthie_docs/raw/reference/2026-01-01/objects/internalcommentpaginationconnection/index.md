---
title: InternalCommentPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/internalcommentpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/internalcommentpaginationconnection/index.md
---

The connection type for InternalComment.

## Fields

[`edges` ](#field-edges)· [`[InternalCommentEdge]` ](/reference/2026-01-01/objects/internalcommentedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[InternalComment]` ](/reference/2026-01-01/objects/internalcomment)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Task.comments`](/reference/2026-01-01/objects/task)

## Definition

```
"""
The connection type for InternalComment.
"""
type InternalCommentPaginationConnection {
  """
  A list of edges.
  """
  edges: [InternalCommentEdge]


  """
  A list of nodes.
  """
  nodes: [InternalComment]


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
