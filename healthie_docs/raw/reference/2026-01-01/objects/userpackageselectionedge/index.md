---
title: UserPackageSelectionEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/userpackageselectionedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/userpackageselectionedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`UserPackageSelection` ](/reference/2026-01-01/objects/userpackageselection)· The item at the end of the edge.

## Used By

[`UserPackageSelectionPaginationConnection.edges`](/reference/2026-01-01/objects/userpackageselectionpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type UserPackageSelectionEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: UserPackageSelection
}
```
