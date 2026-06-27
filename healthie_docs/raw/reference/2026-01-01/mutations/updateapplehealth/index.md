---
title: updateAppleHealth | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateapplehealth/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateapplehealth/index.md
---

Update AppleHealth

## Arguments

[`input` ](#argument-input)· [`updateAppleHealthInput` ](/reference/2026-01-01/input-objects/updateapplehealthinput)· Parameters for updateAppleHealth

## Returns

[`updateAppleHealthPayload`](/reference/2026-01-01/objects/updateapplehealthpayload)

## Example

```
mutation updateAppleHealth($input: updateAppleHealthInput) {
  updateAppleHealth(input: $input) {
    apple_health
    messages
  }
}
```
