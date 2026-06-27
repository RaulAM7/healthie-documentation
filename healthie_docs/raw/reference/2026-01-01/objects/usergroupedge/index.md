---
title: UserGroupEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/usergroupedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/usergroupedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`UserGroup` ](/reference/2026-01-01/objects/usergroup)· The item at the end of the edge.

## Used By

[`UserGroupPaginationConnection.edges`](/reference/2026-01-01/objects/usergrouppaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type UserGroupEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: UserGroup
}
```
