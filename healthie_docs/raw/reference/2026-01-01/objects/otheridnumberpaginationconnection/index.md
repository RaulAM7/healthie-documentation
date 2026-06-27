---
title: OtherIdNumberPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/otheridnumberpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/otheridnumberpaginationconnection/index.md
---

The connection type for OtherIdNumber.

## Fields

[`edges` ](#field-edges)· [`[OtherIdNumberEdge]` ](/reference/2026-01-01/objects/otheridnumberedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OtherIdNumber]` ](/reference/2026-01-01/objects/otheridnumber)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.otherIdNumbers`](/reference/2026-01-01/queries/otheridnumbers)

## Definition

```
"""
The connection type for OtherIdNumber.
"""
type OtherIdNumberPaginationConnection {
  """
  A list of edges.
  """
  edges: [OtherIdNumberEdge]


  """
  A list of nodes.
  """
  nodes: [OtherIdNumber]


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
