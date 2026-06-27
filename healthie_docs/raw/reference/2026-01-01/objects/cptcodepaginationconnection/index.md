---
title: CptCodePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcodepaginationconnection/index.md
---

The connection type for CptCode.

## Fields

[`edges` ](#field-edges)· [`[CptCodeEdge]` ](/reference/2026-01-01/objects/cptcodeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CptCode]` ](/reference/2026-01-01/objects/cptcode)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.cptCodes`](/reference/2026-01-01/queries/cptcodes)

## Definition

```
"""
The connection type for CptCode.
"""
type CptCodePaginationConnection {
  """
  A list of edges.
  """
  edges: [CptCodeEdge]


  """
  A list of nodes.
  """
  nodes: [CptCode]


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
