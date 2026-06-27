---
title: medications | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/medications/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/medications/index.md
---

Fetch paginated medications collection

## Arguments

[`active` ](#argument-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only return active medications.

[`patient_id` ](#argument-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The patient ID to fetch medications for.

[`unreconciled_from_ccda_ingest` ](#argument-unreconciled-from-ccda-ingest)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, only unreconciled objects are returned. Otherwise, they are not included.

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`MedicationTypePaginationConnection`](/reference/2026-01-01/objects/medicationtypepaginationconnection)

## Example

```
query medications(
  $active: Boolean
  $patient_id: ID
  $unreconciled_from_ccda_ingest: Boolean
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  medications(
    active: $active
    patient_id: $patient_id
    unreconciled_from_ccda_ingest: $unreconciled_from_ccda_ingest
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
