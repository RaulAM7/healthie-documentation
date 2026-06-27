---
title: OfferingImageEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringimageedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringimageedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OfferingImage` ](/reference/2026-01-01/objects/offeringimage)· The item at the end of the edge.

## Used By

[`OfferingImagePaginationConnection.edges`](/reference/2026-01-01/objects/offeringimagepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OfferingImageEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OfferingImage
}
```
