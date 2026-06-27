---
title: PayoutAccountEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/payoutaccountedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/payoutaccountedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`PayoutAccount` ](/reference/2026-01-01/objects/payoutaccount)· The item at the end of the edge.

## Used By

[`PayoutAccountPaginationConnection.edges`](/reference/2026-01-01/objects/payoutaccountpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type PayoutAccountEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: PayoutAccount
}
```
