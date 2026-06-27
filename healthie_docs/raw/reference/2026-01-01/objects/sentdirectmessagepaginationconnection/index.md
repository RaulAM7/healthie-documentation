---
title: SentDirectMessagePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentdirectmessagepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentdirectmessagepaginationconnection/index.md
---

The connection type for SentDirectMessage.

## Fields

[`edges` ](#field-edges)· [`[SentDirectMessageEdge]` ](/reference/2026-01-01/objects/sentdirectmessageedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[SentDirectMessage]` ](/reference/2026-01-01/objects/sentdirectmessage)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.sentDirectMessages`](/reference/2026-01-01/queries/sentdirectmessages)

## Definition

```
"""
The connection type for SentDirectMessage.
"""
type SentDirectMessagePaginationConnection {
  """
  A list of edges.
  """
  edges: [SentDirectMessageEdge]


  """
  A list of nodes.
  """
  nodes: [SentDirectMessage]


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
