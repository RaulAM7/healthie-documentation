---
title: CustomModuleFormPaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleformpaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleformpaginationconnection/index.md
---

The connection type for CustomModuleForm.

## Fields

[`edges` ](#field-edges)· [`[CustomModuleFormEdge]` ](/reference/2026-01-01/objects/custommoduleformedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[CustomModuleForm]` ](/reference/2026-01-01/objects/custommoduleform)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.courseItemForms`](/reference/2026-01-01/queries/courseitemforms)

[`Query.customModuleForms`](/reference/2026-01-01/queries/custommoduleforms)

## Definition

```
"""
The connection type for CustomModuleForm.
"""
type CustomModuleFormPaginationConnection {
  """
  A list of edges.
  """
  edges: [CustomModuleFormEdge]


  """
  A list of nodes.
  """
  nodes: [CustomModuleForm]


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
