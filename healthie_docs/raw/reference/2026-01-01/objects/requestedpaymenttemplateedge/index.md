---
title: RequestedPaymentTemplateEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymenttemplateedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymenttemplateedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`RequestedPaymentTemplate` ](/reference/2026-01-01/objects/requestedpaymenttemplate)· The item at the end of the edge.

## Used By

[`RequestedPaymentTemplatePaginationConnection.edges`](/reference/2026-01-01/objects/requestedpaymenttemplatepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type RequestedPaymentTemplateEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: RequestedPaymentTemplate
}
```
