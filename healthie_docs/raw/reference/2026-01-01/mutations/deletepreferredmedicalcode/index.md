---
title: deletePreferredMedicalCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletepreferredmedicalcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletepreferredmedicalcode/index.md
---

Delete favorite CPT/ICD code

## Arguments

[`input` ](#argument-input)· [`deletePreferredMedicalCodeInput` ](/reference/2026-01-01/input-objects/deletepreferredmedicalcodeinput)· Parameters for deletePreferredMedicalCode

## Returns

[`deletePreferredMedicalCodePayload`](/reference/2026-01-01/objects/deletepreferredmedicalcodepayload)

## Example

```
mutation deletePreferredMedicalCode($input: deletePreferredMedicalCodeInput) {
  deletePreferredMedicalCode(input: $input) {
    messages
    preferred_medical_codes
  }
}
```
