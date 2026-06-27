---
title: createDosespotClinician | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdosespotclinician/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createdosespotclinician/index.md
---

Create dosespot clinician

## Arguments

[`input` ](#argument-input)· [`createDosespotClinicianInput` ](/reference/2026-01-01/input-objects/createdosespotclinicianinput)· Parameters for createDosespotClinician

## Returns

[`createDosespotClinicianPayload`](/reference/2026-01-01/objects/createdosespotclinicianpayload)

## Example

```
mutation createDosespotClinician($input: createDosespotClinicianInput) {
  createDosespotClinician(input: $input) {
    dosespot_user
    messages
  }
}
```
