---
title: PharmacyPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/pharmacypaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/pharmacypaginationconnection/index.md
---

The connection type for Pharmacy.

## Fields

[`edges` ](#field-edges)· [`[PharmacyEdge]` ](/reference/2026-01-01/objects/pharmacyedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Pharmacy]` ](/reference/2026-01-01/objects/pharmacy)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.pharmacies`](/reference/2026-01-01/queries/pharmacies)

## Definition

```
"""
The connection type for Pharmacy.
"""
type PharmacyPaginationConnection {
  """
  A list of edges.
  """
  edges: [PharmacyEdge]


  """
  A list of nodes.
  """
  nodes: [Pharmacy]


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
