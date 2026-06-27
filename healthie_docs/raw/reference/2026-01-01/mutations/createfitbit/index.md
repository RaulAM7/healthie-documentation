---
title: createFitbit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfitbit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createfitbit/index.md
---

Create Fitbit

## Arguments

[`input` ](#argument-input)· [`createFitbitInput` ](/reference/2026-01-01/input-objects/createfitbitinput)· Parameters for createFitbit

## Returns

[`createFitbitPayload`](/reference/2026-01-01/objects/createfitbitpayload)

## Example

```
mutation createFitbit($input: createFitbitInput) {
  createFitbit(input: $input) {
    fitbit
    messages
  }
}
```
