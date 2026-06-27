---
title: OfferingImagePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringimagepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringimagepaginationconnection/index.md
---

The connection type for OfferingImage.

## Fields

[`edges` ](#field-edges)· [`[OfferingImageEdge]` ](/reference/2026-01-01/objects/offeringimageedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OfferingImage]` ](/reference/2026-01-01/objects/offeringimage)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.offeringImages`](/reference/2026-01-01/queries/offeringimages)

## Definition

```
"""
The connection type for OfferingImage.
"""
type OfferingImagePaginationConnection {
  """
  A list of edges.
  """
  edges: [OfferingImageEdge]


  """
  A list of nodes.
  """
  nodes: [OfferingImage]


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
