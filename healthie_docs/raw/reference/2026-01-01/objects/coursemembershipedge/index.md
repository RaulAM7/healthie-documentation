---
title: CourseMembershipEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursemembershipedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursemembershipedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CourseMembership` ](/reference/2026-01-01/objects/coursemembership)· The item at the end of the edge.

## Used By

[`CourseMembershipPaginationConnection.edges`](/reference/2026-01-01/objects/coursemembershippaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CourseMembershipEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CourseMembership
}
```
