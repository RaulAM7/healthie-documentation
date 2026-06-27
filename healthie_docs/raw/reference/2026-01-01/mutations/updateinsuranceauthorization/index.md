---
title: updateInsuranceAuthorization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinsuranceauthorization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinsuranceauthorization/index.md
---

update an insurance authorization

## Arguments

[`input` ](#argument-input)· [`updateInsuranceAuthorizationInput` ](/reference/2026-01-01/input-objects/updateinsuranceauthorizationinput)· Parameters for updateInsuranceAuthorization

## Returns

[`updateInsuranceAuthorizationPayload`](/reference/2026-01-01/objects/updateinsuranceauthorizationpayload)

## Example

```
mutation updateInsuranceAuthorization(
  $input: updateInsuranceAuthorizationInput
) {
  updateInsuranceAuthorization(input: $input) {
    insuranceAuthorization
    messages
  }
}
```
