---
title: TagPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/tagpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/tagpaginationconnection/index.md
---

The connection type for Tag.

## Fields

[`edges` ](#field-edges)· [`[TagEdge]` ](/reference/2026-01-01/objects/tagedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Tag]` ](/reference/2026-01-01/objects/tag)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.tagsPaginated`](/reference/2026-01-01/queries/tagspaginated)

## Definition

```
"""
The connection type for Tag.
"""
type TagPaginationConnection {
  """
  A list of edges.
  """
  edges: [TagEdge]


  """
  A list of nodes.
  """
  nodes: [Tag]


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
