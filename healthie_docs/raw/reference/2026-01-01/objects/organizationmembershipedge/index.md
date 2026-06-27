---
title: OrganizationMembershipEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationmembershipedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationmembershipedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OrganizationMembership` ](/reference/2026-01-01/objects/organizationmembership)· The item at the end of the edge.

## Used By

[`OrganizationMembershipPaginationConnection.edges`](/reference/2026-01-01/objects/organizationmembershippaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type OrganizationMembershipEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OrganizationMembership
}
```
