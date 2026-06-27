---
title: SentDirectMessageEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentdirectmessageedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentdirectmessageedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`SentDirectMessage` ](/reference/2026-01-01/objects/sentdirectmessage)· The item at the end of the edge.

## Used By

[`SentDirectMessagePaginationConnection.edges`](/reference/2026-01-01/objects/sentdirectmessagepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type SentDirectMessageEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: SentDirectMessage
}
```
