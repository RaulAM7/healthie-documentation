---
title: RequestedPaymentTemplatePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymenttemplatepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedpaymenttemplatepaginationconnection/index.md
---

The connection type for RequestedPaymentTemplate.

## Fields

[`edges` ](#field-edges)· [`[RequestedPaymentTemplateEdge]` ](/reference/2026-01-01/objects/requestedpaymenttemplateedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[RequestedPaymentTemplate]` ](/reference/2026-01-01/objects/requestedpaymenttemplate)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.invoiceTemplates`](/reference/2026-01-01/queries/invoicetemplates)

## Definition

```
"""
The connection type for RequestedPaymentTemplate.
"""
type RequestedPaymentTemplatePaginationConnection {
  """
  A list of edges.
  """
  edges: [RequestedPaymentTemplateEdge]


  """
  A list of nodes.
  """
  nodes: [RequestedPaymentTemplate]


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
