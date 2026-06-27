---
title: PrescriptionMedicationEdge | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/prescriptionmedicationedge/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/prescriptionmedicationedge/index.md
---

An edge in a connection.

## Fields

[`cursor` ](#field-cursor)· [`Cursor!` ](/reference/2026-01-01/scalars/cursor)· required · A cursor for use in pagination

[`node` ](#field-node)· [`PrescriptionMedication!` ](/reference/2026-01-01/unions/prescriptionmedication)· required · The item at the end of the edge.

## Used By

[`PrescriptionMedicationConnection.edges`](/reference/2026-01-01/objects/prescriptionmedicationconnection)

## Definition

```
"""
An edge in a connection.
"""
type PrescriptionMedicationEdge {
  """
  A cursor for use in pagination
  """
  cursor: Cursor!


  """
  The item at the end of the edge.
  """
  node: PrescriptionMedication!
}
```
