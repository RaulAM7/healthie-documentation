---
title: OfferingPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringpaginationconnection/index.md
---

The connection type for Offering.

## Fields

[`edges` ](#field-edges)· [`[OfferingEdge]` ](/reference/2026-01-01/objects/offeringedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Offering]` ](/reference/2026-01-01/objects/offering)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.offerings`](/reference/2026-01-01/queries/offerings)

## Definition

```
"""
The connection type for Offering.
"""
type OfferingPaginationConnection {
  """
  A list of edges.
  """
  edges: [OfferingEdge]


  """
  A list of nodes.
  """
  nodes: [Offering]


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
