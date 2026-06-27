---
title: PrescriptionMedicationStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/prescriptionmedicationstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/prescriptionmedicationstatus/index.md
---

Prescription medication status type filter enum

## Used By

[`MedicationType.normalized_status`](/reference/2026-01-01/objects/medicationtype)

[`Prescription.normalized_status`](/reference/2026-01-01/objects/prescription)

[`PrescriptionMedicationQueryFiltersInput.normalized_status`](/reference/2026-01-01/input-objects/prescriptionmedicationqueryfiltersinput)

## Definition

```
"""
Prescription medication status type filter enum
"""
enum PrescriptionMedicationStatus {
  """
  (prescriptions and medications)
  """
  ACTIVE


  """
  (prescriptions and medications)
  """
  ERROR


  """
  (prescriptions and medications) has a future start date
  """
  FUTURE


  """
  (prescriptions and medications)
  """
  HIDDEN


  """
  (prescriptions and medications) Marked inactive by the user or past its end date
  """
  INACTIVE


  """
  (prescriptions only)
  """
  PENDING


  """
  (prescriptions only)
  """
  REORDERED
}
```
