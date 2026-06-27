---
title: AcceptedInsurancePlanConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/acceptedinsuranceplanconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/acceptedinsuranceplanconnection/index.md
---

The connection type for AcceptedInsurancePlan.

## Fields

[`edges` ](#field-edges)· [`[AcceptedInsurancePlanEdge]` ](/reference/2026-01-01/objects/acceptedinsuranceplanedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AcceptedInsurancePlan]` ](/reference/2026-01-01/objects/acceptedinsuranceplan)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Organization.accepted_insurance_plans`](/reference/2026-01-01/objects/organization)

## Definition

```
"""
The connection type for AcceptedInsurancePlan.
"""
type AcceptedInsurancePlanConnection {
  """
  A list of edges.
  """
  edges: [AcceptedInsurancePlanEdge]


  """
  A list of nodes.
  """
  nodes: [AcceptedInsurancePlan]


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
