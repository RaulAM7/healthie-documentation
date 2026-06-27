---
title: createAllergySensitivity | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createallergysensitivity/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createallergysensitivity/index.md
---

Create AllergySensitivity

## Arguments

[`input` ](#argument-input)· [`createAllergySensitivityInput` ](/reference/2026-01-01/input-objects/createallergysensitivityinput)· Parameters for createAllergySensitivity

## Returns

[`createAllergySensitivityPayload`](/reference/2026-01-01/objects/createallergysensitivitypayload)

## Example

```
mutation createAllergySensitivity($input: createAllergySensitivityInput) {
  createAllergySensitivity(input: $input) {
    allergy_sensitivity
    duplicate_allergy
    messages
  }
}
```
