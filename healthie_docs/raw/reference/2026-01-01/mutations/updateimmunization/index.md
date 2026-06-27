---
title: updateImmunization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateimmunization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateimmunization/index.md
---

Update an Immunization and return Immunization

## Arguments

[`input` ](#argument-input)· [`updateImmunizationInput` ](/reference/2026-01-01/input-objects/updateimmunizationinput)· Parameters for updateImmunization

## Returns

[`updateImmunizationPayload`](/reference/2026-01-01/objects/updateimmunizationpayload)

## Example

```
mutation updateImmunization($input: updateImmunizationInput) {
  updateImmunization(input: $input) {
    immunization
    messages
  }
}
```
