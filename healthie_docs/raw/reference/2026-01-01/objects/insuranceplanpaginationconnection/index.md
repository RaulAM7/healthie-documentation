---
title: InsurancePlanPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceplanpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceplanpaginationconnection/index.md
---

The connection type for InsurancePlan.

## Fields

[`edges` ](#field-edges)· [`[InsurancePlanEdge]` ](/reference/2026-01-01/objects/insuranceplanedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[InsurancePlan]` ](/reference/2026-01-01/objects/insuranceplan)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Organization.provider_insurance_plans`](/reference/2026-01-01/objects/organization)

[`Query.insurancePlans`](/reference/2026-01-01/queries/insuranceplans)

## Definition

```
"""
The connection type for InsurancePlan.
"""
type InsurancePlanPaginationConnection {
  """
  A list of edges.
  """
  edges: [InsurancePlanEdge]


  """
  A list of nodes.
  """
  nodes: [InsurancePlan]


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
