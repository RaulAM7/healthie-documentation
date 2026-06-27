---
title: WebhookEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/webhookedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/webhookedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`Webhook` ](/reference/2026-01-01/objects/webhook)· The item at the end of the edge.

## Used By

[`WebhookPaginationConnection.edges`](/reference/2026-01-01/objects/webhookpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type WebhookEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: Webhook
}
```
