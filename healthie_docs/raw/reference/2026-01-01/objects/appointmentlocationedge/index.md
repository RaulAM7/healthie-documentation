---
title: AppointmentLocationEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentlocationedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentlocationedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AppointmentLocation` ](/reference/2026-01-01/objects/appointmentlocation)· The item at the end of the edge.

## Used By

[`AppointmentLocationPaginationConnection.edges`](/reference/2026-01-01/objects/appointmentlocationpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AppointmentLocationEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AppointmentLocation
}
```
