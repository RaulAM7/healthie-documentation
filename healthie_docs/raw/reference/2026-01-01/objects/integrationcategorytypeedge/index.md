---
title: IntegrationCategoryTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationcategorytypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/integrationcategorytypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`IntegrationCategoryType` ](/reference/2026-01-01/objects/integrationcategorytype)· The item at the end of the edge.

## Used By

[`IntegrationCategoryTypePaginationConnection.edges`](/reference/2026-01-01/objects/integrationcategorytypepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type IntegrationCategoryTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: IntegrationCategoryType
}
```
