---
title: BillingItemEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/billingitemedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/billingitemedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`BillingItem` ](/reference/2026-01-01/objects/billingitem)· The item at the end of the edge.

## Used By

[`BillingItemPaginationConnection.edges`](/reference/2026-01-01/objects/billingitempaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type BillingItemEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: BillingItem
}
```
