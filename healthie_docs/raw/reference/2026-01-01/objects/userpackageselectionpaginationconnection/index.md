---
title: UserPackageSelectionPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/userpackageselectionpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/userpackageselectionpaginationconnection/index.md
---

The connection type for UserPackageSelection.

## Fields

[`edges` ](#field-edges)· [`[UserPackageSelectionEdge]` ](/reference/2026-01-01/objects/userpackageselectionedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[UserPackageSelection]` ](/reference/2026-01-01/objects/userpackageselection)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.userPackageSelections`](/reference/2026-01-01/queries/userpackageselections)

## Definition

```
"""
The connection type for UserPackageSelection.
"""
type UserPackageSelectionPaginationConnection {
  """
  A list of edges.
  """
  edges: [UserPackageSelectionEdge]


  """
  A list of nodes.
  """
  nodes: [UserPackageSelection]


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
