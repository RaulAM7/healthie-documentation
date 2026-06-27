---
title: ChargeBackPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chargebackpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chargebackpaginationconnection/index.md
---

The connection type for ChargeBack.

## Fields

[`edges` ](#field-edges)· [`[ChargeBackEdge]` ](/reference/2026-01-01/objects/chargebackedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ChargeBack]` ](/reference/2026-01-01/objects/chargeback)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.chargeBacks`](/reference/2026-01-01/queries/chargebacks)

## Definition

```
"""
The connection type for ChargeBack.
"""
type ChargeBackPaginationConnection {
  """
  A list of edges.
  """
  edges: [ChargeBackEdge]


  """
  A list of nodes.
  """
  nodes: [ChargeBack]


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
