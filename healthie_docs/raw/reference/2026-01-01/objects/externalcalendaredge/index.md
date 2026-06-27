---
title: ExternalCalendarEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/externalcalendaredge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/externalcalendaredge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ExternalCalendar` ](/reference/2026-01-01/objects/externalcalendar)· The item at the end of the edge.

## Used By

[`ExternalCalendarConnection.edges`](/reference/2026-01-01/objects/externalcalendarconnection)

## Definition

```
"""
An edge in a connection.
"""
type ExternalCalendarEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ExternalCalendar
}
```
