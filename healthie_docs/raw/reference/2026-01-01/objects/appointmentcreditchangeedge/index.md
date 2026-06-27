---
title: AppointmentCreditChangeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentcreditchangeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentcreditchangeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AppointmentCreditChange` ](/reference/2026-01-01/objects/appointmentcreditchange)· The item at the end of the edge.

## Used By

[`AppointmentCreditChangePaginationConnection.edges`](/reference/2026-01-01/objects/appointmentcreditchangepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AppointmentCreditChangeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AppointmentCreditChange
}
```
