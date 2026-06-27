---
title: AppointmentRequestTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequesttypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/appointmentrequesttypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`AppointmentRequestType` ](/reference/2026-01-01/objects/appointmentrequesttype)· The item at the end of the edge.

## Used By

[`AppointmentRequestTypeConnection.edges`](/reference/2026-01-01/objects/appointmentrequesttypeconnection)

## Definition

```
"""
An edge in a connection.
"""
type AppointmentRequestTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: AppointmentRequestType
}
```
