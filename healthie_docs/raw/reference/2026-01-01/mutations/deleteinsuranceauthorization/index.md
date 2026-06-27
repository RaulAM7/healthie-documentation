---
title: deleteInsuranceAuthorization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteinsuranceauthorization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteinsuranceauthorization/index.md
---

delete an insurance authorization

## Arguments

[`input` ](#argument-input)· [`deleteInsuranceAuthorizationInput` ](/reference/2026-01-01/input-objects/deleteinsuranceauthorizationinput)· Parameters for deleteInsuranceAuthorization

## Returns

[`deleteInsuranceAuthorizationPayload`](/reference/2026-01-01/objects/deleteinsuranceauthorizationpayload)

## Example

```
mutation deleteInsuranceAuthorization(
  $input: deleteInsuranceAuthorizationInput
) {
  deleteInsuranceAuthorization(input: $input) {
    insuranceAuthorization
    messages
  }
}
```
