---
title: InsurancePlanEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceplanedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/insuranceplanedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`InsurancePlan` ](/reference/2026-01-01/objects/insuranceplan)· The item at the end of the edge.

## Used By

[`InsurancePlanPaginationConnection.edges`](/reference/2026-01-01/objects/insuranceplanpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type InsurancePlanEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: InsurancePlan
}
```
