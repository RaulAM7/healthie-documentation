---
title: SuperBillEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/superbilledge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/superbilledge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`SuperBill` ](/reference/2026-01-01/objects/superbill)· The item at the end of the edge.

## Used By

[`SuperBillPaginationConnection.edges`](/reference/2026-01-01/objects/superbillpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type SuperBillEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: SuperBill
}
```
