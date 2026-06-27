---
title: RequestedPaymentEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymentedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymentedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`RequestedPayment` ](/reference/2026-01-01/objects/requestedpayment)· The item at the end of the edge.

## Used By

[`RequestedPaymentPaginationConnection.edges`](/reference/2026-01-01/objects/requestedpaymentpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type RequestedPaymentEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: RequestedPayment
}
```
