---
title: PlaceOfServicePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/placeofservicepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/placeofservicepaginationconnection/index.md
---

The connection type for PlaceOfService.

## Fields

[`edges` ](#field-edges)· [`[PlaceOfServiceEdge]` ](/reference/2026-01-01/objects/placeofserviceedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[PlaceOfService]` ](/reference/2026-01-01/objects/placeofservice)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.placeOfServices`](/reference/2026-01-01/queries/placeofservices)

## Definition

```
"""
The connection type for PlaceOfService.
"""
type PlaceOfServicePaginationConnection {
  """
  A list of edges.
  """
  edges: [PlaceOfServiceEdge]


  """
  A list of nodes.
  """
  nodes: [PlaceOfService]


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
