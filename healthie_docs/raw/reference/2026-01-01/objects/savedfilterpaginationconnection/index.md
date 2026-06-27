---
title: SavedFilterPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/savedfilterpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/savedfilterpaginationconnection/index.md
---

The connection type for SavedFilter.

## Fields

[`edges` ](#field-edges)· [`[SavedFilterEdge]` ](/reference/2026-01-01/objects/savedfilteredge)· A list of edges.

[`nodes` ](#field-nodes)· [`[SavedFilter]` ](/reference/2026-01-01/objects/savedfilter)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.savedFilters`](/reference/2026-01-01/queries/savedfilters)

## Definition

```
"""
The connection type for SavedFilter.
"""
type SavedFilterPaginationConnection {
  """
  A list of edges.
  """
  edges: [SavedFilterEdge]


  """
  A list of nodes.
  """
  nodes: [SavedFilter]


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
