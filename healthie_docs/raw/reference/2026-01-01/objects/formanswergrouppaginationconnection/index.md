---
title: FormAnswerGroupPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergrouppaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/formanswergrouppaginationconnection/index.md
---

The connection type for FormAnswerGroup.

## Fields

[`edges` ](#field-edges)· [`[FormAnswerGroupEdge]` ](/reference/2026-01-01/objects/formanswergroupedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[FormAnswerGroup]` ](/reference/2026-01-01/objects/formanswergroup)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.chartNotes`](/reference/2026-01-01/queries/chartnotes)

[`Query.formAnswerGroups`](/reference/2026-01-01/queries/formanswergroups)

## Definition

```
"""
The connection type for FormAnswerGroup.
"""
type FormAnswerGroupPaginationConnection {
  """
  A list of edges.
  """
  edges: [FormAnswerGroupEdge]


  """
  A list of nodes.
  """
  nodes: [FormAnswerGroup]


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
