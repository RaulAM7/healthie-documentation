---
title: SuperBillPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/superbillpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/superbillpaginationconnection/index.md
---

The connection type for SuperBill.

## Fields

[`edges` ](#field-edges)· [`[SuperBillEdge]` ](/reference/2026-01-01/objects/superbilledge)· A list of edges.

[`nodes` ](#field-nodes)· [`[SuperBill]` ](/reference/2026-01-01/objects/superbill)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.superBills`](/reference/2026-01-01/queries/superbills)

## Definition

```
"""
The connection type for SuperBill.
"""
type SuperBillPaginationConnection {
  """
  A list of edges.
  """
  edges: [SuperBillEdge]


  """
  A list of nodes.
  """
  nodes: [SuperBill]


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
