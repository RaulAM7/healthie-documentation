---
title: PrescriptionMedicationQueryFiltersInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/prescriptionmedicationqueryfiltersinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/prescriptionmedicationqueryfiltersinput/index.md
---

Input type for filtering prescription medications

## Fields

[`end_date_from` ](#field-end-date-from)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The start of the end date filter

[`end_date_to` ](#field-end-date-to)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The end of the end date filter

[`start_date_from` ](#field-start-date-from)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The start of the start date filter

[`start_date_to` ](#field-start-date-to)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The end of the start date filter

[`normalized_status` ](#field-normalized-status)· [`[PrescriptionMedicationStatus]` ](/reference/2026-01-01/enums/prescriptionmedicationstatus)· The normalized status of the medication (e.g., active, inactive, pending)

[`type` ](#field-type)· [`[PrescriptionMedicationTypeEnum]` ](/reference/2026-01-01/enums/prescriptionmedicationtypeenum)· The types of medications (e.g., prescription, medication)

## Used By

[`Query.prescriptionMedications`](/reference/2026-01-01/queries/prescriptionmedications)

## Definition

```
"""
Input type for filtering prescription medications
"""
input PrescriptionMedicationQueryFiltersInput {
  """
  The start of the end date filter
  """
  end_date_from: ISO8601Date


  """
  The end of the end date filter
  """
  end_date_to: ISO8601Date


  """
  The start of the start date filter
  """
  start_date_from: ISO8601Date


  """
  The end of the start date filter
  """
  start_date_to: ISO8601Date


  """
  The normalized status of the medication (e.g., active, inactive, pending)
  """
  normalized_status: [PrescriptionMedicationStatus]


  """
  The types of medications (e.g., prescription, medication)
  """
  type: [PrescriptionMedicationTypeEnum]
}
```
