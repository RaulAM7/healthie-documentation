---
title: OfferingGroupVisibilityEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringgroupvisibilityedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringgroupvisibilityedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OfferingGroupVisibility` ](/reference/2026-01-01/objects/offeringgroupvisibility)· The item at the end of the edge.

## Used By

[`OfferingGroupVisibilityPaginationConnection.edges`](/reference/2026-01-01/objects/offeringgroupvisibilitypaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OfferingGroupVisibilityEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OfferingGroupVisibility
}
```
