---
title: ReceivedDirectMessageEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receiveddirectmessageedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receiveddirectmessageedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ReceivedDirectMessage` ](/reference/2026-01-01/objects/receiveddirectmessage)· The item at the end of the edge.

## Used By

[`ReceivedDirectMessagePaginationConnection.edges`](/reference/2026-01-01/objects/receiveddirectmessagepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ReceivedDirectMessageEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ReceivedDirectMessage
}
```
