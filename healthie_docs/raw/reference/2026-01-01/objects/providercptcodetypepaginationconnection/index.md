---
title: ProviderCptCodeTypePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/providercptcodetypepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/providercptcodetypepaginationconnection/index.md
---

The connection type for ProviderCptCodeType.

## Fields

[`edges` ](#field-edges)· [`[ProviderCptCodeTypeEdge]` ](/reference/2026-01-01/objects/providercptcodetypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ProviderCptCodeType]` ](/reference/2026-01-01/objects/providercptcodetype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.orgProvidersCptCodes`](/reference/2026-01-01/queries/orgproviderscptcodes)

[`Query.providerCptCodes`](/reference/2026-01-01/queries/providercptcodes)

## Definition

```
"""
The connection type for ProviderCptCodeType.
"""
type ProviderCptCodeTypePaginationConnection {
  """
  A list of edges.
  """
  edges: [ProviderCptCodeTypeEdge]


  """
  A list of nodes.
  """
  nodes: [ProviderCptCodeType]


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
