---
title: GoalTemplatePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goaltemplatepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goaltemplatepaginationconnection/index.md
---

The connection type for GoalTemplate.

## Fields

[`edges` ](#field-edges)· [`[GoalTemplateEdge]` ](/reference/2026-01-01/objects/goaltemplateedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[GoalTemplate]` ](/reference/2026-01-01/objects/goaltemplate)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.goalTemplates`](/reference/2026-01-01/queries/goaltemplates)

## Definition

```
"""
The connection type for GoalTemplate.
"""
type GoalTemplatePaginationConnection {
  """
  A list of edges.
  """
  edges: [GoalTemplateEdge]


  """
  A list of nodes.
  """
  nodes: [GoalTemplate]


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
