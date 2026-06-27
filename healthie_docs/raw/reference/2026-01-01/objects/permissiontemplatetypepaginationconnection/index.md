---
title: PermissionTemplateTypePaginationConnection | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/permissiontemplatetypepaginationconnection/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/permissiontemplatetypepaginationconnection/index.md
---

The connection type for PermissionTemplateType.

## Fields

[`edges` ](#field-edges)· [`[PermissionTemplateTypeEdge]` ](/reference/2026-01-01/objects/permissiontemplatetypeedge)· A list of edges.

[`nodes` ](#field-nodes)· [`[PermissionTemplateType]` ](/reference/2026-01-01/objects/permissiontemplatetype)· A list of nodes.

[`page_info` ](#field-page-info)· [`PageInfo!` ](/reference/2026-01-01/objects/pageinfo)· required · Information to aid in pagination.

[`total_count` ](#field-total-count)· [`Int!` ](/reference/2026-01-01/scalars/int)· required · Total count of items.

## Used By

[`Query.permissionTemplates`](/reference/2026-01-01/queries/permissiontemplates)

## Definition

```
"""
The connection type for PermissionTemplateType.
"""
type PermissionTemplateTypePaginationConnection {
  """
  A list of edges.
  """
  edges: [PermissionTemplateTypeEdge]


  """
  A list of nodes.
  """
  nodes: [PermissionTemplateType]


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
