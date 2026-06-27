---
title: createMedication | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmedication/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmedication/index.md
---

Create Medication

## Arguments

[`input` ](#argument-input)· [`createMedicationInput` ](/reference/2026-01-01/input-objects/createmedicationinput)· Parameters for createMedication

## Returns

[`createMedicationPayload`](/reference/2026-01-01/objects/createmedicationpayload)

## Example

```
mutation createMedication($input: createMedicationInput) {
  createMedication(input: $input) {
    medication
    messages
  }
}
```
