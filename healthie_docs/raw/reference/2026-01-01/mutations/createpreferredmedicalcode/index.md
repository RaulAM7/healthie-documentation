---
title: createPreferredMedicalCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpreferredmedicalcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpreferredmedicalcode/index.md
---

Create favorite CPT/ICD code

## Arguments

[`input` ](#argument-input)· [`createPreferredMedicalCodeInput` ](/reference/2026-01-01/input-objects/createpreferredmedicalcodeinput)· Parameters for createPreferredMedicalCode

## Returns

[`createPreferredMedicalCodePayload`](/reference/2026-01-01/objects/createpreferredmedicalcodepayload)

## Example

```
mutation createPreferredMedicalCode($input: createPreferredMedicalCodeInput) {
  createPreferredMedicalCode(input: $input) {
    messages
    preferred_medical_codes
  }
}
```
