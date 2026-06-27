---
title: ConversationMembershipEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembershipedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembershipedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ConversationMembership` ](/reference/2026-01-01/objects/conversationmembership)· The item at the end of the edge.

## Used By

[`ConversationMembershipPaginationConnection.edges`](/reference/2026-01-01/objects/conversationmembershippaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ConversationMembershipEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ConversationMembership
}
```
