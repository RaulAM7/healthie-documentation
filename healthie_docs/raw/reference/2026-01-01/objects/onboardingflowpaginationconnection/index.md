---
title: OnboardingFlowPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingflowpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/onboardingflowpaginationconnection/index.md
---

The connection type for OnboardingFlow.

## Fields

[`edges` ](#field-edges)· [`[OnboardingFlowEdge]` ](/reference/2026-01-01/objects/onboardingflowedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OnboardingFlow]` ](/reference/2026-01-01/objects/onboardingflow)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.onboardingFlows`](/reference/2026-01-01/queries/onboardingflows)

## Definition

```
"""
The connection type for OnboardingFlow.
"""
type OnboardingFlowPaginationConnection {
  """
  A list of edges.
  """
  edges: [OnboardingFlowEdge]


  """
  A list of nodes.
  """
  nodes: [OnboardingFlow]


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
