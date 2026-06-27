---
title: ExternalCalendarConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/externalcalendarconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/externalcalendarconnection/index.md
---

The connection type for ExternalCalendar.

## Fields

[`edges` ](#field-edges)· [`[ExternalCalendarEdge]` ](/reference/2026-01-01/objects/externalcalendaredge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ExternalCalendar]` ](/reference/2026-01-01/objects/externalcalendar)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.externalCalendars`](/reference/2026-01-01/queries/externalcalendars)

## Definition

```
"""
The connection type for ExternalCalendar.
"""
type ExternalCalendarConnection {
  """
  A list of edges.
  """
  edges: [ExternalCalendarEdge]


  """
  A list of nodes.
  """
  nodes: [ExternalCalendar]


  """
  Information to aid in pagination.
  """
  page_info: PageInfo!


  """
  Total count of items.
  """
  total_count: Int!
}
```
