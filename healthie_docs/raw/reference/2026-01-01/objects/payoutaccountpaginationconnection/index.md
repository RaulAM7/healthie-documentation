---
title: PayoutAccountPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/payoutaccountpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/payoutaccountpaginationconnection/index.md
---

The connection type for PayoutAccount.

## Fields

[`edges` ](#field-edges)· [`[PayoutAccountEdge]` ](/reference/2026-01-01/objects/payoutaccountedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[PayoutAccount]` ](/reference/2026-01-01/objects/payoutaccount)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.payoutAccounts`](/reference/2026-01-01/queries/payoutaccounts)

## Definition

```
"""
The connection type for PayoutAccount.
"""
type PayoutAccountPaginationConnection {
  """
  A list of edges.
  """
  edges: [PayoutAccountEdge]


  """
  A list of nodes.
  """
  nodes: [PayoutAccount]


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
