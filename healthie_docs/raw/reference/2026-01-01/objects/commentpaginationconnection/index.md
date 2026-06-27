---
title: CommentPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/commentpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/commentpaginationconnection/index.md
---

The connection type for Comment.

## Fields

[`edges` ](#field-edges)· [`[CommentEdge]` ](/reference/2026-01-01/objects/commentedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Comment]` ](/reference/2026-01-01/objects/comment)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.comments`](/reference/2026-01-01/queries/comments)

## Definition

```
"""
The connection type for Comment.
"""
type CommentPaginationConnection {
  """
  A list of edges.
  """
  edges: [CommentEdge]


  """
  A list of nodes.
  """
  nodes: [Comment]


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
