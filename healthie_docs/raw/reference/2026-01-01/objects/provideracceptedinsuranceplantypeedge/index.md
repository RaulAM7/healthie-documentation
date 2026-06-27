---
title: ProviderAcceptedInsurancePlanTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/provideracceptedinsuranceplantypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/provideracceptedinsuranceplantypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ProviderAcceptedInsurancePlanType` ](/reference/2026-01-01/objects/provideracceptedinsuranceplantype)· The item at the end of the edge.

## Used By

[`ProviderAcceptedInsurancePlanTypePaginationConnection.edges`](/reference/2026-01-01/objects/provideracceptedinsuranceplantypepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ProviderAcceptedInsurancePlanTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ProviderAcceptedInsurancePlanType
}
```
