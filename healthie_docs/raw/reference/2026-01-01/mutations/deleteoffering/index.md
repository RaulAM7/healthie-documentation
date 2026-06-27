---
title: deleteOffering | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteoffering/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteoffering/index.md
---

Destroy an Offering

## Arguments

[`input` ](#argument-input)· [`deleteOfferingInput` ](/reference/2026-01-01/input-objects/deleteofferinginput)· Parameters for deleteOffering

## Returns

[`deleteOfferingPayload`](/reference/2026-01-01/objects/deleteofferingpayload)

## Example

```
mutation deleteOffering($input: deleteOfferingInput) {
  deleteOffering(input: $input) {
    messages
    offering
  }
}
```
