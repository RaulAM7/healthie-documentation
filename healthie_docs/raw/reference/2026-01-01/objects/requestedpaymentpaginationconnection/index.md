---
title: RequestedPaymentPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymentpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymentpaginationconnection/index.md
---

The connection type for RequestedPayment.

## Fields

[`edges` ](#field-edges)· [`[RequestedPaymentEdge]` ](/reference/2026-01-01/objects/requestedpaymentedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[RequestedPayment]` ](/reference/2026-01-01/objects/requestedpayment)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.requestedPayments`](/reference/2026-01-01/queries/requestedpayments)

## Definition

```
"""
The connection type for RequestedPayment.
"""
type RequestedPaymentPaginationConnection {
  """
  A list of edges.
  """
  edges: [RequestedPaymentEdge]


  """
  A list of nodes.
  """
  nodes: [RequestedPayment]


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
