---
title: PrescriptionMedication | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/unions/prescriptionmedication/index
  md: https://docs.gethealthie.com/reference/2026-01-01/unions/prescriptionmedication/index.md
---

Union type representing either a Prescription or Medication

## Possible types

[`MedicationType`](#field-medicationtype)

[`Prescription`](#field-prescription)

## Used By

[`PrescriptionMedicationConnection.nodes`](/reference/2026-01-01/objects/prescriptionmedicationconnection)

[`PrescriptionMedicationEdge.node`](/reference/2026-01-01/objects/prescriptionmedicationedge)

## Definition

```
"""
Union type representing either a Prescription or Medication
"""
union PrescriptionMedication = MedicationType | Prescription
```
