---
title: deleteProviderAcceptedInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteprovideracceptedinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteprovideracceptedinsuranceplan/index.md
---

Delete an existing provider accepted insurance plan

## Arguments

[`input` ](#argument-input)· [`deleteProviderAcceptedInsurancePlanInput` ](/reference/2026-01-01/input-objects/deleteprovideracceptedinsuranceplaninput)· Parameters for deleteProviderAcceptedInsurancePlan

## Returns

[`deleteProviderAcceptedInsurancePlanPayload`](/reference/2026-01-01/objects/deleteprovideracceptedinsuranceplanpayload)

## Example

```
mutation deleteProviderAcceptedInsurancePlan(
  $input: deleteProviderAcceptedInsurancePlanInput
) {
  deleteProviderAcceptedInsurancePlan(input: $input) {
    messages
    providerAcceptedInsurancePlan
  }
}
```
