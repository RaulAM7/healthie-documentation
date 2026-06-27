---
title: createImmunization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createimmunization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createimmunization/index.md
---

Create an Immunization

## Arguments

[`input` ](#argument-input)· [`createImmunizationInput` ](/reference/2026-01-01/input-objects/createimmunizationinput)· Parameters for createImmunization

## Returns

[`createImmunizationPayload`](/reference/2026-01-01/objects/createimmunizationpayload)

## Example

```
mutation createImmunization($input: createImmunizationInput) {
  createImmunization(input: $input) {
    immunization
    messages
  }
}
```
