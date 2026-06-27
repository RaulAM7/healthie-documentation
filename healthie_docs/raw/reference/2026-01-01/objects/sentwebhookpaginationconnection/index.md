---
title: SentWebhookPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentwebhookpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentwebhookpaginationconnection/index.md
---

The connection type for SentWebhook.

## Fields

[`edges` ](#field-edges)· [`[SentWebhookEdge]` ](/reference/2026-01-01/objects/sentwebhookedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[SentWebhook]` ](/reference/2026-01-01/objects/sentwebhook)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.sentWebhooks`](/reference/2026-01-01/queries/sentwebhooks)

## Definition

```
"""
The connection type for SentWebhook.
"""
type SentWebhookPaginationConnection {
  """
  A list of edges.
  """
  edges: [SentWebhookEdge]


  """
  A list of nodes.
  """
  nodes: [SentWebhook]


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
