---
title: SentWebhookEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/sentwebhookedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/sentwebhookedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`SentWebhook` ](/reference/2026-01-01/objects/sentwebhook)· The item at the end of the edge.

## Used By

[`SentWebhookPaginationConnection.edges`](/reference/2026-01-01/objects/sentwebhookpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type SentWebhookEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: SentWebhook
}
```
