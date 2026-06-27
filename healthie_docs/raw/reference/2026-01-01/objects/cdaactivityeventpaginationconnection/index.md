---
title: CdaActivityEventPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cdaactivityeventpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cdaactivityeventpaginationconnection/index.md
---

The connection type for CdaActivityEvent.

## Fields

[`edges` ](#field-edges)· [`[CdaActivityEventEdge]` ](/reference/2026-01-01/objects/cdaactivityeventedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CdaActivityEvent]` ](/reference/2026-01-01/objects/cdaactivityevent)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.cdaActivityEvents`](/reference/2026-01-01/queries/cdaactivityevents)

## Definition

```
"""
The connection type for CdaActivityEvent.
"""
type CdaActivityEventPaginationConnection {
  """
  A list of edges.
  """
  edges: [CdaActivityEventEdge]


  """
  A list of nodes.
  """
  nodes: [CdaActivityEvent]


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
