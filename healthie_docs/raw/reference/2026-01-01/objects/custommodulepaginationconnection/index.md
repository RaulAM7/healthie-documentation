---
title: CustomModulePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommodulepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommodulepaginationconnection/index.md
---

The connection type for CustomModule.

## Fields

[`edges` ](#field-edges)· [`[CustomModuleEdge]` ](/reference/2026-01-01/objects/custommoduleedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CustomModule]` ](/reference/2026-01-01/objects/custommodule)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.customModules`](/reference/2026-01-01/queries/custommodules)

## Definition

```
"""
The connection type for CustomModule.
"""
type CustomModulePaginationConnection {
  """
  A list of edges.
  """
  edges: [CustomModuleEdge]


  """
  A list of nodes.
  """
  nodes: [CustomModule]


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
