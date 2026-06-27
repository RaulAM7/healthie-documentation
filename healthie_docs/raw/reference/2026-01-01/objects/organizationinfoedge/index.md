---
title: OrganizationInfoEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationinfoedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationinfoedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OrganizationInfo` ](/reference/2026-01-01/objects/organizationinfo)· The item at the end of the edge.

## Used By

[`OrganizationInfoPaginationConnection.edges`](/reference/2026-01-01/objects/organizationinfopaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OrganizationInfoEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OrganizationInfo
}
```
