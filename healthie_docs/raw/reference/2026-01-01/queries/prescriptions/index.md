---
title: prescriptions | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/prescriptions/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/prescriptions/index.md
---

deprecated Use \`prescriptionMedications\` instead

Fetch an array of prescriptions for a given patient pulled from DoseSpot

## Arguments

[`patient_id` ](#argument-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the patient whose prescriptions are being fetched

[`status` ](#argument-status)· [`String` ](/reference/2026-01-01/scalars/string)· Filter prescriptions by status (e.g. active, inactive, pending, error, hidden). Passing "all" will return prescriptions of any status.

[`make_unique` ](#argument-make-unique)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Filter to most recent by written date prescription based on dispensable drug id + product name, defaults as true, ignored unless passed with a status in \[active, inactive, pending, error, hidden]

[`current_only` ](#argument-current-only)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Filter out any future effective dated prescriptions, defaults to true

## Returns

[`[Prescription!]`](/reference/2026-01-01/objects/prescription)

## Example

```
query prescriptions(
  $patient_id: ID
  $status: String
  $make_unique: Boolean
  $current_only: Boolean
) {
  prescriptions(
    patient_id: $patient_id
    status: $status
    make_unique: $make_unique
    current_only: $current_only
  ) {
    clinic_id
    comment
    date_inactive
    date_written
    days_supply
    directions
    dispensable_drug_id
    dispense_unit_id
    display_name
    dosage
    dose_form
    drug_classification
    effective_date
    eligibility_id
    encounter
    error_ignored
    first_prescription_diagnosis
    formulary
    free_text_type
    id
    is_rx_renewal
    is_urgent
    last_fill_date
    medication_status
    ndc
    no_substitutions
    non_dose_spot_prescription_id
    normalized_status
    otc
    patient_medication_id
    pharmacy
    pharmacy_notes
    prescriber_agent_id
    prescriber_id
    prescriber_name
    product_name
    quantity
    refills
    route
    rx_reference_number
    rx_renewal_note
    rxcui
    schedule
    second_prescription_diagnosis
    status
    supervisor_id
    supply_id
    type
    unit
  }
}
```
