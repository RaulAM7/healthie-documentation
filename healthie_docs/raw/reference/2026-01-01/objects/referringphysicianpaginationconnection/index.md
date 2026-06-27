---
title: ReferringPhysicianPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/referringphysicianpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/referringphysicianpaginationconnection/index.md
---

The connection type for ReferringPhysician.

## Fields

[`edges` ](#field-edges)· [`[ReferringPhysicianEdge]` ](/reference/2026-01-01/objects/referringphysicianedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[ReferringPhysician]` ](/reference/2026-01-01/objects/referringphysician)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.referringPhysicians`](/reference/2026-01-01/queries/referringphysicians)

## Definition

```
"""
The connection type for ReferringPhysician.
"""
type ReferringPhysicianPaginationConnection {
  """
  A list of edges.
  """
  edges: [ReferringPhysicianEdge]


  """
  A list of nodes.
  """
  nodes: [ReferringPhysician]


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
