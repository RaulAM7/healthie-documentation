---
title: prescription | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/prescription/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/prescription/index.md
---

Fetch a prescription for a given patient and prescription ID pulled from DoseSpot

## Arguments

[`patient_id` ](#argument-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the patient whose prescription is being fetched

[`prescription_id` ](#argument-prescription-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The DoseSpot prescription ID to fetch

## Returns

[`Prescription`](/reference/2026-01-01/objects/prescription)

## Example

```
query prescription($patient_id: ID, $prescription_id: ID) {
  prescription(patient_id: $patient_id, prescription_id: $prescription_id) {
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
