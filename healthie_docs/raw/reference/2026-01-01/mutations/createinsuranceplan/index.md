---
title: createInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinsuranceplan/index.md
---

Create Insurance Plan

## Arguments

[`input` ](#argument-input)· [`createInsurancePlanInput` ](/reference/2026-01-01/input-objects/createinsuranceplaninput)· Parameters for createInsurancePlan

## Returns

[`createInsurancePlanPayload`](/reference/2026-01-01/objects/createinsuranceplanpayload)

## Example

```
mutation createInsurancePlan($input: createInsurancePlanInput) {
  createInsurancePlan(input: $input) {
    insurance_plan
    messages
  }
}
```
