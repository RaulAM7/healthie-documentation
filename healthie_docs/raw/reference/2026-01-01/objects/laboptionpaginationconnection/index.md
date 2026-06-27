---
title: LabOptionPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/laboptionpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/laboptionpaginationconnection/index.md
---

The connection type for LabOption.

## Fields

[`edges` ](#field-edges)· [`[LabOptionEdge]` ](/reference/2026-01-01/objects/laboptionedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[LabOption]` ](/reference/2026-01-01/objects/laboption)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.labOptions`](/reference/2026-01-01/queries/laboptions)

## Definition

```
"""
The connection type for LabOption.
"""
type LabOptionPaginationConnection {
  """
  A list of edges.
  """
  edges: [LabOptionEdge]


  """
  A list of nodes.
  """
  nodes: [LabOption]


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
