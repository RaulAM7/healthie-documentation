---
title: EraServiceLineConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/eraservicelineconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/eraservicelineconnection/index.md
---

The connection type for EraServiceLine.

## Fields

[`edges` ](#field-edges)· [`[EraServiceLineEdge]` ](/reference/2026-01-01/objects/eraservicelineedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[EraServiceLine]` ](/reference/2026-01-01/objects/eraserviceline)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Era.era_service_lines`](/reference/2026-01-01/objects/era)

## Definition

```
"""
The connection type for EraServiceLine.
"""
type EraServiceLineConnection {
  """
  A list of edges.
  """
  edges: [EraServiceLineEdge]


  """
  A list of nodes.
  """
  nodes: [EraServiceLine]


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
