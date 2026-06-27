---
title: ConversationMembershipPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembershippaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/conversationmembershippaginationconnection/index.md
---

The connection type for ConversationMembership.

## Fields

[`edges` ](#field-edges)· [`[ConversationMembershipEdge]` ](/reference/2026-01-01/objects/conversationmembershipedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ConversationMembership]` ](/reference/2026-01-01/objects/conversationmembership)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.conversationMembershipInvitees`](/reference/2026-01-01/queries/conversationmembershipinvitees)

[`Query.conversationMemberships`](/reference/2026-01-01/queries/conversationmemberships)

## Definition

```
"""
The connection type for ConversationMembership.
"""
type ConversationMembershipPaginationConnection {
  """
  A list of edges.
  """
  edges: [ConversationMembershipEdge]


  """
  A list of nodes.
  """
  nodes: [ConversationMembership]


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
