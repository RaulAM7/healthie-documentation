---
title: OrganizationFeeScheduleCptCodeTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`OrganizationFeeScheduleCptCodeType` ](/reference/2026-01-01/objects/organizationfeeschedulecptcodetype)· The item at the end of the edge.

## Used By

[`OrganizationFeeScheduleCptCodeTypeConnection.edges`](/reference/2026-01-01/objects/organizationfeeschedulecptcodetypeconnection)

## Definition

```
"""
An edge in a connection.
"""
type OrganizationFeeScheduleCptCodeTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: OrganizationFeeScheduleCptCodeType
}
```
