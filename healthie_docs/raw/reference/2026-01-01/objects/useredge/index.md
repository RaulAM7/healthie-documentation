---
title: UserEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/useredge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/useredge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`User` ](/reference/2026-01-01/objects/user)· The item at the end of the edge.

## Used By

[`UserConnection.edges`](/reference/2026-01-01/objects/userconnection)

## Definition

```
"""
An edge in a connection.
"""
type UserEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: User
}
```
