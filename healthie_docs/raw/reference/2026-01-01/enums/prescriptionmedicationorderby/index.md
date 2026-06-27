---
title: PrescriptionMedicationOrderBy | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/prescriptionmedicationorderby/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/prescriptionmedicationorderby/index.md
---

Enum for sorting prescription medications

## Used By

[`Query.prescriptionMedications`](/reference/2026-01-01/queries/prescriptionmedications)

## Definition

```
"""
Enum for sorting prescription medications
"""
enum PrescriptionMedicationOrderBy {
  """
  Sort by name in ascending order
  """
  NAME_ASC


  """
  Sort by name in descending order
  """
  NAME_DESC


  """
  Sort by start date in ascending order
  """
  START_DATE_ASC


  """
  Sort by start date in descending order
  """
  START_DATE_DESC


  """
  Sort by status in ascending order
  """
  STATUS_ASC


  """
  Sort by status in descending order
  """
  STATUS_DESC


  """
  Sort by active status first
  """
  ACTIVE_FIRST


  """
  Sort by inactive status first
  """
  INACTIVE_FIRST


  """
  Sort by error status first
  """
  ERROR_FIRST


  """
  Sort by pending status first
  """
  PENDING_FIRST
}
```
