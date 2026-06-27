---
title: ScheduledUserPackageSelectionPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/scheduleduserpackageselectionpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/scheduleduserpackageselectionpaginationconnection/index.md
---

The connection type for ScheduledUserPackageSelection.

## Fields

[`edges` ](#field-edges)· [`[ScheduledUserPackageSelectionEdge]` ](/reference/2026-01-01/objects/scheduleduserpackageselectionedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ScheduledUserPackageSelection]` ](/reference/2026-01-01/objects/scheduleduserpackageselection)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.scheduledUserPackageSelections`](/reference/2026-01-01/queries/scheduleduserpackageselections)

## Definition

```
"""
The connection type for ScheduledUserPackageSelection.
"""
type ScheduledUserPackageSelectionPaginationConnection {
  """
  A list of edges.
  """
  edges: [ScheduledUserPackageSelectionEdge]


  """
  A list of nodes.
  """
  nodes: [ScheduledUserPackageSelection]


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
