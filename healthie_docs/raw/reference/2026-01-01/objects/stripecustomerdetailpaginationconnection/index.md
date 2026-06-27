---
title: StripeCustomerDetailPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecustomerdetailpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripecustomerdetailpaginationconnection/index.md
---

The connection type for StripeCustomerDetail.

## Fields

[`edges` ](#field-edges)· [`[StripeCustomerDetailEdge]` ](/reference/2026-01-01/objects/stripecustomerdetailedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[StripeCustomerDetail]` ](/reference/2026-01-01/objects/stripecustomerdetail)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.cardIssues`](/reference/2026-01-01/queries/cardissues)

[`Query.stripeCustomerDetails`](/reference/2026-01-01/queries/stripecustomerdetails)

## Definition

```
"""
The connection type for StripeCustomerDetail.
"""
type StripeCustomerDetailPaginationConnection {
  """
  A list of edges.
  """
  edges: [StripeCustomerDetailEdge]


  """
  A list of nodes.
  """
  nodes: [StripeCustomerDetail]


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
