---
title: createProviderAcceptedInsurancePlans | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createprovideracceptedinsuranceplans/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createprovideracceptedinsuranceplans/index.md
---

Create one or more accepted insurance plan associations for a specific provider.

## Arguments

[`input` ](#argument-input)· [`createProviderAcceptedInsurancePlansInput` ](/reference/2026-01-01/input-objects/createprovideracceptedinsuranceplansinput)· Parameters for createProviderAcceptedInsurancePlans

## Returns

[`createProviderAcceptedInsurancePlansPayload`](/reference/2026-01-01/objects/createprovideracceptedinsuranceplanspayload)

## Example

```
mutation createProviderAcceptedInsurancePlans(
  $input: createProviderAcceptedInsurancePlansInput
) {
  createProviderAcceptedInsurancePlans(input: $input) {
    messages
    provider_accepted_insurance_plans
  }
}
```
