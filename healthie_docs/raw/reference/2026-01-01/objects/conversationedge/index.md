---
title: ConversationEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Conversation` ](/reference/2026-01-01/objects/conversation)· The item at the end of the edge.

## Used By

[`ConversationPaginationConnection.edges`](/reference/2026-01-01/objects/conversationpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ConversationEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Conversation
}
```
