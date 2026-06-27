---
title: ReceivedFaxEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receivedfaxedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receivedfaxedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ReceivedFax` ](/reference/2026-01-01/objects/receivedfax)· The item at the end of the edge.

## Used By

[`ReceivedFaxPaginationConnection.edges`](/reference/2026-01-01/objects/receivedfaxpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ReceivedFaxEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ReceivedFax
}
```
