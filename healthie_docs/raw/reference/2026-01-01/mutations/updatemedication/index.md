---
title: updateMedication | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemedication/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemedication/index.md
---

Update Medication

## Arguments

[`input` ](#argument-input)· [`updateMedicationInput` ](/reference/2026-01-01/input-objects/updatemedicationinput)· Parameters for updateMedication

## Returns

[`updateMedicationPayload`](/reference/2026-01-01/objects/updatemedicationpayload)

## Example

```
mutation updateMedication($input: updateMedicationInput) {
  updateMedication(input: $input) {
    medication
    messages
  }
}
```
