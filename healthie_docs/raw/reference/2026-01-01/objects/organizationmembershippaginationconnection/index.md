---
title: OrganizationMembershipPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationmembershippaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationmembershippaginationconnection/index.md
---

The connection type for OrganizationMembership.

## Fields

[`edges` ](#field-edges)· [`[OrganizationMembershipEdge]` ](/reference/2026-01-01/objects/organizationmembershipedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[OrganizationMembership]` ](/reference/2026-01-01/objects/organizationmembership)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Organization.organization_memberships`](/reference/2026-01-01/objects/organization)

[`Query.organizationMemberships`](/reference/2026-01-01/queries/organizationmemberships)

## Definition

```
"""
The connection type for OrganizationMembership.
"""
type OrganizationMembershipPaginationConnection {
  """
  A list of edges.
  """
  edges: [OrganizationMembershipEdge]


  """
  A list of nodes.
  """
  nodes: [OrganizationMembership]


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
