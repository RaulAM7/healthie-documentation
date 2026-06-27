---
title: patientEncounter | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/patientencounter/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/patientencounter/index.md
---

Fetch a patient encounter

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`appointment_id` ](#argument-appointment-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`patient_id` ](#argument-patient-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`PatientEncounter`](/reference/2026-01-01/objects/patientencounter)

## Example

```
query patientEncounter($id: ID, $appointment_id: ID, $patient_id: ID) {
  patientEncounter(
    id: $id
    appointment_id: $appointment_id
    patient_id: $patient_id
  ) {
    appointment
    charting_notes
    cms1500
    id
    patient
    requested_payments
  }
}
```
