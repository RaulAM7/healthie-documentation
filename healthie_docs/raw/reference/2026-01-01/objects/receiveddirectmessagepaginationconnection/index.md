---
title: ReceivedDirectMessagePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receiveddirectmessagepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receiveddirectmessagepaginationconnection/index.md
---

The connection type for ReceivedDirectMessage.

## Fields

[`edges` ](#field-edges)· [`[ReceivedDirectMessageEdge]` ](/reference/2026-01-01/objects/receiveddirectmessageedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ReceivedDirectMessage]` ](/reference/2026-01-01/objects/receiveddirectmessage)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.receivedDirectMessages`](/reference/2026-01-01/queries/receiveddirectmessages)

## Definition

```
"""
The connection type for ReceivedDirectMessage.
"""
type ReceivedDirectMessagePaginationConnection {
  """
  A list of edges.
  """
  edges: [ReceivedDirectMessageEdge]


  """
  A list of nodes.
  """
  nodes: [ReceivedDirectMessage]


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
