---
title: createAppleHealth | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createapplehealth/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createapplehealth/index.md
---

Create AppleHealth

## Arguments

[`input` ](#argument-input)· [`createAppleHealthInput` ](/reference/2026-01-01/input-objects/createapplehealthinput)· Parameters for createAppleHealth

## Returns

[`createAppleHealthPayload`](/reference/2026-01-01/objects/createapplehealthpayload)

## Example

```
mutation createAppleHealth($input: createAppleHealthInput) {
  createAppleHealth(input: $input) {
    apple_health
    messages
  }
}
```
