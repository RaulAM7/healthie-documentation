---
title: OfferingCouponEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcouponedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringcouponedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OfferingCoupon` ](/reference/2026-01-01/objects/offeringcoupon)· The item at the end of the edge.

## Used By

[`OfferingCouponPaginationConnection.edges`](/reference/2026-01-01/objects/offeringcouponpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OfferingCouponEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OfferingCoupon
}
```
