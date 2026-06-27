---
title: ProviderCptCodeTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/providercptcodetypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/providercptcodetypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`ProviderCptCodeType` ](/reference/2026-01-01/objects/providercptcodetype)· The item at the end of the edge.

## Used By

[`ProviderCptCodeTypePaginationConnection.edges`](/reference/2026-01-01/objects/providercptcodetypepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type ProviderCptCodeTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: ProviderCptCodeType
}
```
