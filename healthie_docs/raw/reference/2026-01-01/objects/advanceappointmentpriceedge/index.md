---
title: AdvanceAppointmentPriceEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/advanceappointmentpriceedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/advanceappointmentpriceedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AdvanceAppointmentPrice` ](/reference/2026-01-01/objects/advanceappointmentprice)· The item at the end of the edge.

## Used By

[`AdvanceAppointmentPricePaginationConnection.edges`](/reference/2026-01-01/objects/advanceappointmentpricepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AdvanceAppointmentPriceEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AdvanceAppointmentPrice
}
```
