---
title: OrganizationInfoPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationinfopaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationinfopaginationconnection/index.md
---

The connection type for OrganizationInfo.

## Fields

[`edges` ](#field-edges)· [`[OrganizationInfoEdge]` ](/reference/2026-01-01/objects/organizationinfoedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OrganizationInfo]` ](/reference/2026-01-01/objects/organizationinfo)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Organization.organization_infos`](/reference/2026-01-01/objects/organization)

## Definition

```
"""
The connection type for OrganizationInfo.
"""
type OrganizationInfoPaginationConnection {
  """
  A list of edges.
  """
  edges: [OrganizationInfoEdge]


  """
  A list of nodes.
  """
  nodes: [OrganizationInfo]


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
