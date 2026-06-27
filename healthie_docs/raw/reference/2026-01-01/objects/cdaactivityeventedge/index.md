---
title: CdaActivityEventEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cdaactivityeventedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cdaactivityeventedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CdaActivityEvent` ](/reference/2026-01-01/objects/cdaactivityevent)· The item at the end of the edge.

## Used By

[`CdaActivityEventPaginationConnection.edges`](/reference/2026-01-01/objects/cdaactivityeventpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CdaActivityEventEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CdaActivityEvent
}
```
