---
title: LocationPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/locationpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/locationpaginationconnection/index.md
---

The connection type for Location.

## Fields

[`edges` ](#field-edges)· [`[LocationEdge]` ](/reference/2026-01-01/objects/locationedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Location]` ](/reference/2026-01-01/objects/location)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.locations`](/reference/2026-01-01/queries/locations)

## Definition

```
"""
The connection type for Location.
"""
type LocationPaginationConnection {
  """
  A list of edges.
  """
  edges: [LocationEdge]


  """
  A list of nodes.
  """
  nodes: [Location]


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
