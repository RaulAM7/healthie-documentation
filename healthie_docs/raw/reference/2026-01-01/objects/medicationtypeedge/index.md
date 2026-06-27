---
title: MedicationTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationtypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationtypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`MedicationType` ](/reference/2026-01-01/objects/medicationtype)· The item at the end of the edge.

## Used By

[`MedicationTypePaginationConnection.edges`](/reference/2026-01-01/objects/medicationtypepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type MedicationTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: MedicationType
}
```
