---
title: RecurringPaymentPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringpaymentpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringpaymentpaginationconnection/index.md
---

The connection type for RecurringPayment.

## Fields

[`edges` ](#field-edges)· [`[RecurringPaymentEdge]` ](/reference/2026-01-01/objects/recurringpaymentedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[RecurringPayment]` ](/reference/2026-01-01/objects/recurringpayment)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.recurringPayments`](/reference/2026-01-01/queries/recurringpayments)

## Definition

```
"""
The connection type for RecurringPayment.
"""
type RecurringPaymentPaginationConnection {
  """
  A list of edges.
  """
  edges: [RecurringPaymentEdge]


  """
  A list of nodes.
  """
  nodes: [RecurringPayment]


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
