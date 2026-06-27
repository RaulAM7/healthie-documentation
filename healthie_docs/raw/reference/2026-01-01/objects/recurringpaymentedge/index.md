---
title: RecurringPaymentEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringpaymentedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringpaymentedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`RecurringPayment` ](/reference/2026-01-01/objects/recurringpayment)· The item at the end of the edge.

## Used By

[`RecurringPaymentPaginationConnection.edges`](/reference/2026-01-01/objects/recurringpaymentpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type RecurringPaymentEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: RecurringPayment
}
```
