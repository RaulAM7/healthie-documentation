---
title: StateLicenseEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/statelicenseedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/statelicenseedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`StateLicense` ](/reference/2026-01-01/objects/statelicense)· The item at the end of the edge.

## Used By

[`StateLicensePaginationConnection.edges`](/reference/2026-01-01/objects/statelicensepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type StateLicenseEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: StateLicense
}
```
