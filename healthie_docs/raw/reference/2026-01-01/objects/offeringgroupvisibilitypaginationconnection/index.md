---
title: OfferingGroupVisibilityPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringgroupvisibilitypaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringgroupvisibilitypaginationconnection/index.md
---

The connection type for OfferingGroupVisibility.

## Fields

[`edges` ](#field-edges)· [`[OfferingGroupVisibilityEdge]` ](/reference/2026-01-01/objects/offeringgroupvisibilityedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OfferingGroupVisibility]` ](/reference/2026-01-01/objects/offeringgroupvisibility)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.offeringGroupVisibilities`](/reference/2026-01-01/queries/offeringgroupvisibilities)

## Definition

```
"""
The connection type for OfferingGroupVisibility.
"""
type OfferingGroupVisibilityPaginationConnection {
  """
  A list of edges.
  """
  edges: [OfferingGroupVisibilityEdge]


  """
  A list of nodes.
  """
  nodes: [OfferingGroupVisibility]


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
