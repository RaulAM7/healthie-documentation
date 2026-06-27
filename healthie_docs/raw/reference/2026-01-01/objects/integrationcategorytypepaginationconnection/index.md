---
title: IntegrationCategoryTypePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationcategorytypepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationcategorytypepaginationconnection/index.md
---

The connection type for IntegrationCategoryType.

## Fields

[`edges` ](#field-edges)· [`[IntegrationCategoryTypeEdge]` ](/reference/2026-01-01/objects/integrationcategorytypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[IntegrationCategoryType]` ](/reference/2026-01-01/objects/integrationcategorytype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.integrationsList`](/reference/2026-01-01/queries/integrationslist)

## Definition

```
"""
The connection type for IntegrationCategoryType.
"""
type IntegrationCategoryTypePaginationConnection {
  """
  A list of edges.
  """
  edges: [IntegrationCategoryTypeEdge]


  """
  A list of nodes.
  """
  nodes: [IntegrationCategoryType]


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
