---
title: deleteInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteinsuranceplan/index.md
---

Delete Insurance Plan

## Arguments

[`input` ](#argument-input)· [`deleteInsurancePlanInput` ](/reference/2026-01-01/input-objects/deleteinsuranceplaninput)· Parameters for deleteInsurancePlan

## Returns

[`deleteInsurancePlanPayload`](/reference/2026-01-01/objects/deleteinsuranceplanpayload)

## Example

```
mutation deleteInsurancePlan($input: deleteInsurancePlanInput) {
  deleteInsurancePlan(input: $input) {
    insurance_plan
    messages
  }
}
```
