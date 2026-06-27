---
title: deleteMedication | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemedication/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemedication/index.md
---

Destroy Medication

## Arguments

[`input` ](#argument-input)· [`destroyMedicationInput` ](/reference/2026-01-01/input-objects/destroymedicationinput)· Parameters for destroyMedication

## Returns

[`destroyMedicationPayload`](/reference/2026-01-01/objects/destroymedicationpayload)

## Example

```
mutation deleteMedication($input: destroyMedicationInput) {
  deleteMedication(input: $input) {
    medication
    messages
  }
}
```
