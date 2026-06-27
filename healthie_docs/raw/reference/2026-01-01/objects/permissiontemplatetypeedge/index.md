---
title: PermissionTemplateTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/permissiontemplatetypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/permissiontemplatetypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`PermissionTemplateType` ](/reference/2026-01-01/objects/permissiontemplatetype)· The item at the end of the edge.

## Used By

[`PermissionTemplateTypePaginationConnection.edges`](/reference/2026-01-01/objects/permissiontemplatetypepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type PermissionTemplateTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: PermissionTemplateType
}
```
