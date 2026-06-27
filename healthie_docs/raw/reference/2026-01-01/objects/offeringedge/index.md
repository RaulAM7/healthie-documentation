---
title: OfferingEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Offering` ](/reference/2026-01-01/objects/offering)· The item at the end of the edge.

## Used By

[`OfferingPaginationConnection.edges`](/reference/2026-01-01/objects/offeringpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OfferingEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Offering
}
```
