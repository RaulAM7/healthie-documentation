---
title: CustomModuleFormEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleformedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/custommoduleformedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CustomModuleForm` ](/reference/2026-01-01/objects/custommoduleform)· The item at the end of the edge.

## Used By

[`CustomModuleFormPaginationConnection.edges`](/reference/2026-01-01/objects/custommoduleformpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CustomModuleFormEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CustomModuleForm
}
```
