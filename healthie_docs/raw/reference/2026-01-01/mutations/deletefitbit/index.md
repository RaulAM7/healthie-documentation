---
title: deleteFitbit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefitbit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletefitbit/index.md
---

Destroy Fitbit

## Arguments

[`input` ](#argument-input)· [`deleteFitbitInput` ](/reference/2026-01-01/input-objects/deletefitbitinput)· Parameters for deleteFitbit

## Returns

[`deleteFitbitPayload`](/reference/2026-01-01/objects/deletefitbitpayload)

## Example

```
mutation deleteFitbit($input: deleteFitbitInput) {
  deleteFitbit(input: $input) {
    fitbit
    messages
  }
}
```
