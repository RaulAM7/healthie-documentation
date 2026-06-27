---
title: ChargeDisputeTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/chargedisputetypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/chargedisputetypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ChargeDisputeType` ](/reference/2026-01-01/objects/chargedisputetype)· The item at the end of the edge.

## Used By

[`ChargeDisputeTypeConnection.edges`](/reference/2026-01-01/objects/chargedisputetypeconnection)

## Definition

```
"""
An edge in a connection.
"""
type ChargeDisputeTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ChargeDisputeType
}
```
