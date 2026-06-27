---
title: createChangeHealthPatient | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createchangehealthpatient/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createchangehealthpatient/index.md
---

creates ChangeHealth patient record

## Arguments

[`input` ](#argument-input)· [`CreateChangeHealthPatientInput` ](/reference/2026-01-01/input-objects/createchangehealthpatientinput)· Parameters for CreateChangeHealthPatient

## Returns

[`CreateChangeHealthPatientPayload`](/reference/2026-01-01/objects/createchangehealthpatientpayload)

## Example

```
mutation createChangeHealthPatient($input: CreateChangeHealthPatientInput) {
  createChangeHealthPatient(input: $input) {
    messages
    user
  }
}
```
