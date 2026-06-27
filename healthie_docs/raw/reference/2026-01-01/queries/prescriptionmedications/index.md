---
title: prescriptionMedications | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/prescriptionmedications/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/prescriptionmedications/index.md
---

Fetches combined list of prescriptions and medications

## Arguments

[`patient_id` ](#argument-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the patient to fetch medications for

[`filters` ](#argument-filters)· [`PrescriptionMedicationQueryFiltersInput` ](/reference/2026-01-01/input-objects/prescriptionmedicationqueryfiltersinput)· Advanced filter options for querying prescription medications

[`keyword` ](#argument-keyword)· [`String` ](/reference/2026-01-01/scalars/string)· Search medications by name

[`order_by` ](#argument-order-by)· [`PrescriptionMedicationOrderBy` ](/reference/2026-01-01/enums/prescriptionmedicationorderby)· Sorting parameter for the medications

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· number of items to return

[`after` ](#argument-after)· [`Cursor` ](/reference/2026-01-01/scalars/cursor)· Cursor to fetch results after

## Returns

[`PrescriptionMedicationConnection`](/reference/2026-01-01/objects/prescriptionmedicationconnection)

## Example

```
query prescriptionMedications(
  $patient_id: ID
  $filters: PrescriptionMedicationQueryFiltersInput
  $keyword: String
  $order_by: PrescriptionMedicationOrderBy
  $first: Int
  $after: Cursor
) {
  prescriptionMedications(
    patient_id: $patient_id
    filters: $filters
    keyword: $keyword
    order_by: $order_by
    first: $first
    after: $after
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
