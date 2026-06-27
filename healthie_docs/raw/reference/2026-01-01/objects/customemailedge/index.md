---
title: CustomEmailEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/customemailedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/customemailedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`CustomEmail` ](/reference/2026-01-01/objects/customemail)· The item at the end of the edge.

## Used By

[`CustomEmailPaginationConnection.edges`](/reference/2026-01-01/objects/customemailpaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type CustomEmailEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: CustomEmail
}
```
