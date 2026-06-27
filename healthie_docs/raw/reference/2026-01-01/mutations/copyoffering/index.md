---
title: copyOffering | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/copyoffering/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/copyoffering/index.md
---

Copy an Offering

## Arguments

[`input` ](#argument-input)· [`copyOfferingInput` ](/reference/2026-01-01/input-objects/copyofferinginput)· Parameters for copyOffering

## Returns

[`copyOfferingPayload`](/reference/2026-01-01/objects/copyofferingpayload)

## Example

```
mutation copyOffering($input: copyOfferingInput) {
  copyOffering(input: $input) {
    messages
    offering
  }
}
```
