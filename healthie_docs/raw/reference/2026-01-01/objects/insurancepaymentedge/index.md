---
title: InsurancePaymentEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insurancepaymentedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insurancepaymentedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`InsurancePayment` ](/reference/2026-01-01/objects/insurancepayment)· The item at the end of the edge.

## Used By

[`InsurancePaymentConnection.edges`](/reference/2026-01-01/objects/insurancepaymentconnection)

## Definition

```
"""
An edge in a connection.
"""
type InsurancePaymentEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: InsurancePayment
}
```
