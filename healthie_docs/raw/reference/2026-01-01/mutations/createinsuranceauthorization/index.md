---
title: createInsuranceAuthorization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinsuranceauthorization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinsuranceauthorization/index.md
---

create an insurance authorization

## Arguments

[`input` ](#argument-input)· [`createInsuranceAuthorizationInput` ](/reference/2026-01-01/input-objects/createinsuranceauthorizationinput)· Parameters for createInsuranceAuthorization

## Returns

[`createInsuranceAuthorizationPayload`](/reference/2026-01-01/objects/createinsuranceauthorizationpayload)

## Example

```
mutation createInsuranceAuthorization(
  $input: createInsuranceAuthorizationInput
) {
  createInsuranceAuthorization(input: $input) {
    insuranceAuthorization
    messages
  }
}
```
