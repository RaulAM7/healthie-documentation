---
title: updateFitbit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefitbit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatefitbit/index.md
---

Update Fitbit

## Arguments

[`input` ](#argument-input)· [`updateFitbitInput` ](/reference/2026-01-01/input-objects/updatefitbitinput)· Parameters for updateFitbit

## Returns

[`updateFitbitPayload`](/reference/2026-01-01/objects/updatefitbitpayload)

## Example

```
mutation updateFitbit($input: updateFitbitInput) {
  updateFitbit(input: $input) {
    fitbit
    messages
  }
}
```
