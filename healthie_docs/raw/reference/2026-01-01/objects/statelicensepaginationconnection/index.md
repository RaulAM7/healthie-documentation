---
title: StateLicensePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/statelicensepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/statelicensepaginationconnection/index.md
---

The connection type for StateLicense.

## Fields

[`edges` ](#field-edges)· [`[StateLicenseEdge]` ](/reference/2026-01-01/objects/statelicenseedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[StateLicense]` ](/reference/2026-01-01/objects/statelicense)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.stateLicenses`](/reference/2026-01-01/queries/statelicenses)

## Definition

```
"""
The connection type for StateLicense.
"""
type StateLicensePaginationConnection {
  """
  A list of edges.
  """
  edges: [StateLicenseEdge]


  """
  A list of nodes.
  """
  nodes: [StateLicense]


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
