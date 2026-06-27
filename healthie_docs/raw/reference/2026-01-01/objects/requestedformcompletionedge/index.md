---
title: RequestedFormCompletionEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformcompletionedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/requestedformcompletionedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`RequestedFormCompletion` ](/reference/2026-01-01/objects/requestedformcompletion)· The item at the end of the edge.

## Used By

[`RequestedFormCompletionPaginationConnection.edges`](/reference/2026-01-01/objects/requestedformcompletionpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type RequestedFormCompletionEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: RequestedFormCompletion
}
```
