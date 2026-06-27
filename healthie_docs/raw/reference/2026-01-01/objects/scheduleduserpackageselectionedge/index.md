---
title: ScheduledUserPackageSelectionEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/scheduleduserpackageselectionedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/scheduleduserpackageselectionedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ScheduledUserPackageSelection` ](/reference/2026-01-01/objects/scheduleduserpackageselection)· The item at the end of the edge.

## Used By

[`ScheduledUserPackageSelectionPaginationConnection.edges`](/reference/2026-01-01/objects/scheduleduserpackageselectionpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ScheduledUserPackageSelectionEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ScheduledUserPackageSelection
}
```
