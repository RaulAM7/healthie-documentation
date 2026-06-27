---
title: ConversationPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationpaginationconnection/index.md
---

The connection type for Conversation.

## Fields

[`edges` ](#field-edges)· [`[ConversationEdge]` ](/reference/2026-01-01/objects/conversationedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Conversation]` ](/reference/2026-01-01/objects/conversation)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.conversations`](/reference/2026-01-01/queries/conversations)

## Definition

```
"""
The connection type for Conversation.
"""
type ConversationPaginationConnection {
  """
  A list of edges.
  """
  edges: [ConversationEdge]


  """
  A list of nodes.
  """
  nodes: [Conversation]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
