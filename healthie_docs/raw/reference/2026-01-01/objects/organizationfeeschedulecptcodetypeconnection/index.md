---
title: OrganizationFeeScheduleCptCodeTypeConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeconnection/index.md
---

The connection type for OrganizationFeeScheduleCptCodeType.

## Fields

[`edges` ](#field-edges)· [`[OrganizationFeeScheduleCptCodeTypeEdge]` ](/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OrganizationFeeScheduleCptCodeType]` ](/reference/2026-01-01/objects/organizationfeeschedulecptcodetype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.organizationFeeScheduleCptCodes`](/reference/2026-01-01/queries/organizationfeeschedulecptcodes)

## Definition

```
"""
The connection type for OrganizationFeeScheduleCptCodeType.
"""
type OrganizationFeeScheduleCptCodeTypeConnection {
  """
  A list of edges.
  """
  edges: [OrganizationFeeScheduleCptCodeTypeEdge]


  """
  A list of nodes.
  """
  nodes: [OrganizationFeeScheduleCptCodeType]


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
