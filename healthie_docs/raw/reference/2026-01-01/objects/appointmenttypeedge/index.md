---
title: AppointmentTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmenttypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AppointmentType` ](/reference/2026-01-01/objects/appointmenttype)· The item at the end of the edge.

## Used By

[`AppointmentTypePaginationConnection.edges`](/reference/2026-01-01/objects/appointmenttypepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type AppointmentTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AppointmentType
}
```
