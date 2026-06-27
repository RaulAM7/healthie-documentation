---
title: ReceiptLineItemPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receiptlineitempaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receiptlineitempaginationconnection/index.md
---

The connection type for ReceiptLineItem.

## Fields

[`edges` ](#field-edges)· [`[ReceiptLineItemEdge]` ](/reference/2026-01-01/objects/receiptlineitemedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ReceiptLineItem]` ](/reference/2026-01-01/objects/receiptlineitem)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.receiptLineItems`](/reference/2026-01-01/queries/receiptlineitems)

## Definition

```
"""
The connection type for ReceiptLineItem.
"""
type ReceiptLineItemPaginationConnection {
  """
  A list of edges.
  """
  edges: [ReceiptLineItemEdge]


  """
  A list of nodes.
  """
  nodes: [ReceiptLineItem]


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
