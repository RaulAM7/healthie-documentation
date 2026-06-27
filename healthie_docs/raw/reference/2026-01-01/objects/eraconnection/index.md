---
title: EraConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/eraconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/eraconnection/index.md
---

The connection type for Era.

## Fields

[`edges` ](#field-edges)· [`[EraEdge]` ](/reference/2026-01-01/objects/eraedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Era]` ](/reference/2026-01-01/objects/era)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Cms1500.eras`](/reference/2026-01-01/objects/cms1500)

## Definition

```
"""
The connection type for Era.
"""
type EraConnection {
  """
  A list of edges.
  """
  edges: [EraEdge]


  """
  A list of nodes.
  """
  nodes: [Era]


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
