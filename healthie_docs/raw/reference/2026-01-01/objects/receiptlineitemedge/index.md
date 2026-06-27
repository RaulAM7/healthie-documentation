---
title: ReceiptLineItemEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receiptlineitemedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receiptlineitemedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ReceiptLineItem` ](/reference/2026-01-01/objects/receiptlineitem)· The item at the end of the edge.

## Used By

[`ReceiptLineItemPaginationConnection.edges`](/reference/2026-01-01/objects/receiptlineitempaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ReceiptLineItemEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ReceiptLineItem
}
```
