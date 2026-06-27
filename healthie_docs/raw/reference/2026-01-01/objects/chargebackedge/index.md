---
title: ChargeBackEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chargebackedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chargebackedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ChargeBack` ](/reference/2026-01-01/objects/chargeback)· The item at the end of the edge.

## Used By

[`ChargeBackPaginationConnection.edges`](/reference/2026-01-01/objects/chargebackpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ChargeBackEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ChargeBack
}
```
