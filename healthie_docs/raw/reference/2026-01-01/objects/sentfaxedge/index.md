---
title: SentFaxEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentfaxedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentfaxedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`SentFax` ](/reference/2026-01-01/objects/sentfax)· The item at the end of the edge.

## Used By

[`SentFaxPaginationConnection.edges`](/reference/2026-01-01/objects/sentfaxpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type SentFaxEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: SentFax
}
```
