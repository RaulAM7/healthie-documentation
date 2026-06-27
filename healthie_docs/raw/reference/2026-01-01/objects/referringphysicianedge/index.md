---
title: ReferringPhysicianEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/referringphysicianedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/referringphysicianedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ReferringPhysician` ](/reference/2026-01-01/objects/referringphysician)· The item at the end of the edge.

## Used By

[`ReferringPhysicianPaginationConnection.edges`](/reference/2026-01-01/objects/referringphysicianpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ReferringPhysicianEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ReferringPhysician
}
```
