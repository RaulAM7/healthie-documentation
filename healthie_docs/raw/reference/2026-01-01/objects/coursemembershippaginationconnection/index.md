---
title: CourseMembershipPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursemembershippaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursemembershippaginationconnection/index.md
---

The connection type for CourseMembership.

## Fields

[`edges` ](#field-edges)· [`[CourseMembershipEdge]` ](/reference/2026-01-01/objects/coursemembershipedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CourseMembership]` ](/reference/2026-01-01/objects/coursemembership)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.courseClients`](/reference/2026-01-01/queries/courseclients)

[`Query.courseMemberships`](/reference/2026-01-01/queries/coursememberships)

[`Query.ungroupedCourseMemberships`](/reference/2026-01-01/queries/ungroupedcoursememberships)

## Definition

```
"""
The connection type for CourseMembership.
"""
type CourseMembershipPaginationConnection {
  """
  A list of edges.
  """
  edges: [CourseMembershipEdge]


  """
  A list of nodes.
  """
  nodes: [CourseMembership]


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
