---
title: ReceivedFaxPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/receivedfaxpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/receivedfaxpaginationconnection/index.md
---

The connection type for ReceivedFax.

## Fields

[`edges` ](#field-edges)· [`[ReceivedFaxEdge]` ](/reference/2026-01-01/objects/receivedfaxedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ReceivedFax]` ](/reference/2026-01-01/objects/receivedfax)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.receivedFaxes`](/reference/2026-01-01/queries/receivedfaxes)

## Definition

```
"""
The connection type for ReceivedFax.
"""
type ReceivedFaxPaginationConnection {
  """
  A list of edges.
  """
  edges: [ReceivedFaxEdge]


  """
  A list of nodes.
  """
  nodes: [ReceivedFax]


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
