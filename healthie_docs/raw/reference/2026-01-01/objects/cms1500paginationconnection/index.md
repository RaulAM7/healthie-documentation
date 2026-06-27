---
title: Cms1500PaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500paginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cms1500paginationconnection/index.md
---

The connection type for Cms1500.

## Fields

[`edges` ](#field-edges)· [`[Cms1500Edge]` ](/reference/2026-01-01/objects/cms1500edge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Cms1500]` ](/reference/2026-01-01/objects/cms1500)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.cms1500s`](/reference/2026-01-01/queries/cms1500s)

## Definition

```
"""
The connection type for Cms1500.
"""
type Cms1500PaginationConnection {
  """
  A list of edges.
  """
  edges: [Cms1500Edge]


  """
  A list of nodes.
  """
  nodes: [Cms1500]


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
