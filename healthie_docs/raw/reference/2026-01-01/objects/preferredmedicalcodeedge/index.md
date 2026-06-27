---
title: PreferredMedicalCodeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/preferredmedicalcodeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/preferredmedicalcodeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`PreferredMedicalCode` ](/reference/2026-01-01/objects/preferredmedicalcode)· The item at the end of the edge.

## Used By

[`PreferredMedicalCodePaginationConnection.edges`](/reference/2026-01-01/objects/preferredmedicalcodepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type PreferredMedicalCodeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: PreferredMedicalCode
}
```
