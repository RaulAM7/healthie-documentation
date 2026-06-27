---
title: createAcceptedInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createacceptedinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createacceptedinsuranceplan/index.md
---

Create Accepted Insurance Plans

## Arguments

[`input` ](#argument-input)· [`createAcceptedInsurancePlanInput` ](/reference/2026-01-01/input-objects/createacceptedinsuranceplaninput)· Parameters for createAcceptedInsurancePlan

## Returns

[`createAcceptedInsurancePlanPayload`](/reference/2026-01-01/objects/createacceptedinsuranceplanpayload)

## Example

```
mutation createAcceptedInsurancePlan($input: createAcceptedInsurancePlanInput) {
  createAcceptedInsurancePlan(input: $input) {
    accepted_insurance_plans
    appointment_setting
    messages
  }
}
```
