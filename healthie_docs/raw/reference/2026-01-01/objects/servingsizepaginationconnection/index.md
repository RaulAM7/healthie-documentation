---
title: ServingSizePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/servingsizepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/servingsizepaginationconnection/index.md
---

The connection type for ServingSize.

## Fields

[`edges` ](#field-edges)· [`[ServingSizeEdge]` ](/reference/2026-01-01/objects/servingsizeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ServingSize]` ](/reference/2026-01-01/objects/servingsize)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.servingSizes`](/reference/2026-01-01/queries/servingsizes)

## Definition

```
"""
The connection type for ServingSize.
"""
type ServingSizePaginationConnection {
  """
  A list of edges.
  """
  edges: [ServingSizeEdge]


  """
  A list of nodes.
  """
  nodes: [ServingSize]


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
