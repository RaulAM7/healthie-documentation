---
title: ApiKeyPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/apikeypaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/apikeypaginationconnection/index.md
---

The connection type for ApiKey.

## Fields

[`edges` ](#field-edges)· [`[ApiKeyEdge]` ](/reference/2026-01-01/objects/apikeyedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ApiKey]` ](/reference/2026-01-01/objects/apikey)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.apiKeys`](/reference/2026-01-01/queries/apikeys)

[`User.api_keys`](/reference/2026-01-01/objects/user)

## Definition

```
"""
The connection type for ApiKey.
"""
type ApiKeyPaginationConnection {
  """
  A list of edges.
  """
  edges: [ApiKeyEdge]


  """
  A list of nodes.
  """
  nodes: [ApiKey]


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
