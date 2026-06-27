---
title: BillingItemPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/billingitempaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/billingitempaginationconnection/index.md
---

The connection type for BillingItem.

## Fields

[`edges` ](#field-edges)· [`[BillingItemEdge]` ](/reference/2026-01-01/objects/billingitemedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[BillingItem]` ](/reference/2026-01-01/objects/billingitem)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.billingItems`](/reference/2026-01-01/queries/billingitems)

[`Query.offeringBillingItems`](/reference/2026-01-01/queries/offeringbillingitems)

## Definition

```
"""
The connection type for BillingItem.
"""
type BillingItemPaginationConnection {
  """
  A list of edges.
  """
  edges: [BillingItemEdge]


  """
  A list of nodes.
  """
  nodes: [BillingItem]


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
