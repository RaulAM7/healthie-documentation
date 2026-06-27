---
title: OfferingCouponPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcouponpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcouponpaginationconnection/index.md
---

The connection type for OfferingCoupon.

## Fields

[`edges` ](#field-edges)· [`[OfferingCouponEdge]` ](/reference/2026-01-01/objects/offeringcouponedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OfferingCoupon]` ](/reference/2026-01-01/objects/offeringcoupon)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.offeringCoupons`](/reference/2026-01-01/queries/offeringcoupons)

## Definition

```
"""
The connection type for OfferingCoupon.
"""
type OfferingCouponPaginationConnection {
  """
  A list of edges.
  """
  edges: [OfferingCouponEdge]


  """
  A list of nodes.
  """
  nodes: [OfferingCoupon]


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
