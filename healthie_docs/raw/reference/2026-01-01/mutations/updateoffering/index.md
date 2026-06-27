---
title: updateOffering | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateoffering/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateoffering/index.md
---

Update an Offering

## Arguments

[`input` ](#argument-input)· [`updateOfferingInput` ](/reference/2026-01-01/input-objects/updateofferinginput)· Parameters for updateOffering

## Returns

[`updateOfferingPayload`](/reference/2026-01-01/objects/updateofferingpayload)

## Example

```
mutation updateOffering($input: updateOfferingInput) {
  updateOffering(input: $input) {
    messages
    offering
  }
}
```
