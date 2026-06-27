---
title: AcceptedInsurancePlanEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/acceptedinsuranceplanedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/acceptedinsuranceplanedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AcceptedInsurancePlan` ](/reference/2026-01-01/objects/acceptedinsuranceplan)· The item at the end of the edge.

## Used By

[`AcceptedInsurancePlanConnection.edges`](/reference/2026-01-01/objects/acceptedinsuranceplanconnection)

## Definition

```
"""
An edge in a connection.
"""
type AcceptedInsurancePlanEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AcceptedInsurancePlan
}
```
