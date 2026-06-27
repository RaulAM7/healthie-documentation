---
title: dosespot_ui_link | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/dosespot-ui-link/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/dosespot-ui-link/index.md
---

Fetch the iframe link to prescribe for a given patient (patient must have valid phone\_number, dob, location.line1, location.city, location.state, and location.zip)

## Arguments

[`patient_id` ](#argument-patient-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Healthie user ID of the patient to prescribe for.

[`form_answer_group_id` ](#argument-form-answer-group-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Optional ID of the form\_answer\_group to associate with the DoseSpot session.

## Returns

[`String`](/reference/2026-01-01/scalars/string)

## Example

```
query dosespot_ui_link($patient_id: ID, $form_answer_group_id: ID) {
  dosespot_ui_link(
    patient_id: $patient_id
    form_answer_group_id: $form_answer_group_id
  )
}
```
