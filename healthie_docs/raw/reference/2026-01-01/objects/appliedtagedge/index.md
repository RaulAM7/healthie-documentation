---
title: AppliedTagEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appliedtagedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appliedtagedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AppliedTag` ](/reference/2026-01-01/objects/appliedtag)· The item at the end of the edge.

## Used By

[`AppliedTagPaginationConnection.edges`](/reference/2026-01-01/objects/appliedtagpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AppliedTagEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AppliedTag
}
```
