---
title: ClaimEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/claimedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/claimedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Claim` ](/reference/2026-01-01/objects/claim)· The item at the end of the edge.

## Used By

[`ClaimPaginationConnection.edges`](/reference/2026-01-01/objects/claimpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ClaimEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Claim
}
```
