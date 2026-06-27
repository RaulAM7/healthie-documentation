---
title: AutoTaskGeneratorPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/autotaskgeneratorpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/autotaskgeneratorpaginationconnection/index.md
---

The connection type for AutoTaskGenerator.

## Fields

[`edges` ](#field-edges)· [`[AutoTaskGeneratorEdge]` ](/reference/2026-01-01/objects/autotaskgeneratoredge)· A list of edges.

[`nodes` ](#field-nodes)· [`[AutoTaskGenerator]` ](/reference/2026-01-01/objects/autotaskgenerator)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.autoTaskGenerators`](/reference/2026-01-01/queries/autotaskgenerators)

## Definition

```
"""
The connection type for AutoTaskGenerator.
"""
type AutoTaskGeneratorPaginationConnection {
  """
  A list of edges.
  """
  edges: [AutoTaskGeneratorEdge]


  """
  A list of nodes.
  """
  nodes: [AutoTaskGenerator]


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
