---
title: ApiKeyEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/apikeyedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/apikeyedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ApiKey` ](/reference/2026-01-01/objects/apikey)· The item at the end of the edge.

## Used By

[`ApiKeyPaginationConnection.edges`](/reference/2026-01-01/objects/apikeypaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ApiKeyEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ApiKey
}
```
