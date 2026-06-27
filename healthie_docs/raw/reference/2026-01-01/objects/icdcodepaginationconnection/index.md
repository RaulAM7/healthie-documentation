---
title: IcdCodePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/icdcodepaginationconnection/index.md
---

The connection type for IcdCode.

## Fields

[`edges` ](#field-edges)· [`[IcdCodeEdge]` ](/reference/2026-01-01/objects/icdcodeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[IcdCode]` ](/reference/2026-01-01/objects/icdcode)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.icdCodes`](/reference/2026-01-01/queries/icdcodes)

## Definition

```
"""
The connection type for IcdCode.
"""
type IcdCodePaginationConnection {
  """
  A list of edges.
  """
  edges: [IcdCodeEdge]


  """
  A list of nodes.
  """
  nodes: [IcdCode]


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
