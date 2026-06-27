---
title: deleteAppleHealth | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteapplehealth/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteapplehealth/index.md
---

Destroy AppleHealth

## Arguments

[`input` ](#argument-input)· [`deleteAppleHealthInput` ](/reference/2026-01-01/input-objects/deleteapplehealthinput)· Parameters for deleteAppleHealth

## Returns

[`deleteAppleHealthPayload`](/reference/2026-01-01/objects/deleteapplehealthpayload)

## Example

```
mutation deleteAppleHealth($input: deleteAppleHealthInput) {
  deleteAppleHealth(input: $input) {
    apple_health
    messages
  }
}
```
