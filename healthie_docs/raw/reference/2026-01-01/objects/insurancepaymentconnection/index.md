---
title: InsurancePaymentConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insurancepaymentconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insurancepaymentconnection/index.md
---

The connection type for InsurancePayment.

## Fields

[`edges` ](#field-edges)· [`[InsurancePaymentEdge]` ](/reference/2026-01-01/objects/insurancepaymentedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[InsurancePayment]` ](/reference/2026-01-01/objects/insurancepayment)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.insurancePayments`](/reference/2026-01-01/queries/insurancepayments)

## Definition

```
"""
The connection type for InsurancePayment.
"""
type InsurancePaymentConnection {
  """
  A list of edges.
  """
  edges: [InsurancePaymentEdge]


  """
  A list of nodes.
  """
  nodes: [InsurancePayment]


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
