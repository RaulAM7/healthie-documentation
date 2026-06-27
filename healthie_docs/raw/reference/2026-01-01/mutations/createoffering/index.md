---
title: createOffering | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createoffering/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createoffering/index.md
---

create offering

## Arguments

[`input` ](#argument-input)· [`createOfferingInput!` ](/reference/2026-01-01/input-objects/createofferinginput)· required · Parameters for createOffering

## Returns

[`createOfferingPayload`](/reference/2026-01-01/objects/createofferingpayload)

## Example

```
mutation createOffering($input: createOfferingInput!) {
  createOffering(input: $input) {
    messages
    offering
  }
}
```
