---
title: updateAllergySensitivity | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateallergysensitivity/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateallergysensitivity/index.md
---

Update AllergySensitivity

## Arguments

[`input` ](#argument-input)· [`updateAllergySensitivityInput` ](/reference/2026-01-01/input-objects/updateallergysensitivityinput)· Parameters for updateAllergySensitivity

## Returns

[`updateAllergySensitivityPayload`](/reference/2026-01-01/objects/updateallergysensitivitypayload)

## Example

```
mutation updateAllergySensitivity($input: updateAllergySensitivityInput) {
  updateAllergySensitivity(input: $input) {
    allergy_sensitivity
    duplicate_allergy
    messages
  }
}
```
