---
title: StripeCustomerDetailEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecustomerdetailedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecustomerdetailedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`StripeCustomerDetail` ](/reference/2026-01-01/objects/stripecustomerdetail)· The item at the end of the edge.

## Used By

[`StripeCustomerDetailPaginationConnection.edges`](/reference/2026-01-01/objects/stripecustomerdetailpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type StripeCustomerDetailEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: StripeCustomerDetail
}
```
