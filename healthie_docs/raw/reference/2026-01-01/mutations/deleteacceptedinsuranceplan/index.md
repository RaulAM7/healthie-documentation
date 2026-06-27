---
title: deleteAcceptedInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteacceptedinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteacceptedinsuranceplan/index.md
---

Destroy Accepted Insurance Plan

## Arguments

[`input` ](#argument-input)· [`deleteAcceptedInsurancePlanInput` ](/reference/2026-01-01/input-objects/deleteacceptedinsuranceplaninput)· Parameters for deleteAcceptedInsurancePlan

## Returns

[`deleteAcceptedInsurancePlanPayload`](/reference/2026-01-01/objects/deleteacceptedinsuranceplanpayload)

## Example

```
mutation deleteAcceptedInsurancePlan($input: deleteAcceptedInsurancePlanInput) {
  deleteAcceptedInsurancePlan(input: $input) {
    accepted_insurance_plan
    appointment_setting
    messages
  }
}
```
