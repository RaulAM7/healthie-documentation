---
title: ProviderAcceptedInsurancePlanTypePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/provideracceptedinsuranceplantypepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/provideracceptedinsuranceplantypepaginationconnection/index.md
---

The connection type for ProviderAcceptedInsurancePlanType.

## Fields

[`edges` ](#field-edges)· [`[ProviderAcceptedInsurancePlanTypeEdge]` ](/reference/2026-01-01/objects/provideracceptedinsuranceplantypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ProviderAcceptedInsurancePlanType]` ](/reference/2026-01-01/objects/provideracceptedinsuranceplantype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.providerAcceptedInsurancePlans`](/reference/2026-01-01/queries/provideracceptedinsuranceplans)

## Definition

```
"""
The connection type for ProviderAcceptedInsurancePlanType.
"""
type ProviderAcceptedInsurancePlanTypePaginationConnection {
  """
  A list of edges.
  """
  edges: [ProviderAcceptedInsurancePlanTypeEdge]


  """
  A list of nodes.
  """
  nodes: [ProviderAcceptedInsurancePlanType]


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
