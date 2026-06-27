---
title: surescriptsReportedMedicationHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/surescriptsreportedmedicationhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/surescriptsreportedmedicationhistory/index.md
---

Fetch medication history from the Surescripts history (via Dosespot). Patient consent must be confirmed via the API before calling.

## Arguments

[`patient_id` ](#argument-patient-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`start_date` ](#argument-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Defaults to 6 months ago

[`end_date` ](#argument-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Defaults to end of current day

[`after` ](#argument-after)· [`Cursor`](/reference/2026-01-01/scalars/cursor)

[`before` ](#argument-before)· [`Cursor`](/reference/2026-01-01/scalars/cursor)

## Returns

[`MedicationHistoryTypePaginationConnection`](/reference/2026-01-01/objects/medicationhistorytypepaginationconnection)

## Example

```
query surescriptsReportedMedicationHistory(
  $patient_id: ID!
  $start_date: ISO8601DateTime
  $end_date: ISO8601DateTime
  $after: Cursor
  $before: Cursor
) {
  surescriptsReportedMedicationHistory(
    patient_id: $patient_id
    start_date: $start_date
    end_date: $end_date
    after: $after
    before: $before
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
