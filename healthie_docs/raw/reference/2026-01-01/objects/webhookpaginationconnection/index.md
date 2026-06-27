---
title: WebhookPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/webhookpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/webhookpaginationconnection/index.md
---

The connection type for Webhook.

## Fields

[`edges` ](#field-edges)· [`[WebhookEdge]` ](/reference/2026-01-01/objects/webhookedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[Webhook]` ](/reference/2026-01-01/objects/webhook)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.webhooks`](/reference/2026-01-01/queries/webhooks)

## Definition

```
"""
The connection type for Webhook.
"""
type WebhookPaginationConnection {
  """
  A list of edges.
  """
  edges: [WebhookEdge]


  """
  A list of nodes.
  """
  nodes: [Webhook]


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
