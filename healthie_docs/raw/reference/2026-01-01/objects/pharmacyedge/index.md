---
title: PharmacyEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/pharmacyedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/pharmacyedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Pharmacy` ](/reference/2026-01-01/objects/pharmacy)· The item at the end of the edge.

## Used By

[`PharmacyPaginationConnection.edges`](/reference/2026-01-01/objects/pharmacypaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type PharmacyEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Pharmacy
}
```
