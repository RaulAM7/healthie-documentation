---
title: MedicationHistoryTypeEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationhistorytypeedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationhistorytypeedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`MedicationHistoryType` ](/reference/2026-01-01/objects/medicationhistorytype)· The item at the end of the edge.

## Used By

[`MedicationHistoryTypePaginationConnection.edges`](/reference/2026-01-01/objects/medicationhistorytypepaginationconnection)

## Definition

```
"""
An edge in a connection.
"""
type MedicationHistoryTypeEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: MedicationHistoryType
}
```
