---
title: deleteAllergySensitivity | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteallergysensitivity/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteallergysensitivity/index.md
---

Destroy AllergySensitivity

## Arguments

[`input` ](#argument-input)· [`deleteAllergySensitivityInput` ](/reference/2026-01-01/input-objects/deleteallergysensitivityinput)· Parameters for deleteAllergySensitivity

## Returns

[`deleteAllergySensitivityPayload`](/reference/2026-01-01/objects/deleteallergysensitivitypayload)

## Example

```
mutation deleteAllergySensitivity($input: deleteAllergySensitivityInput) {
  deleteAllergySensitivity(input: $input) {
    allergy_sensitivity
    messages
  }
}
```
