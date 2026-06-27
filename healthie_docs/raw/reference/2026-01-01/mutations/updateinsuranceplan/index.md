---
title: updateInsurancePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinsuranceplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinsuranceplan/index.md
---

Update Insurance Plan

## Arguments

[`input` ](#argument-input)· [`updateInsurancePlanInput` ](/reference/2026-01-01/input-objects/updateinsuranceplaninput)· Parameters for updateInsurancePlan

## Returns

[`updateInsurancePlanPayload`](/reference/2026-01-01/objects/updateinsuranceplanpayload)

## Example

```
mutation updateInsurancePlan($input: updateInsurancePlanInput) {
  updateInsurancePlan(input: $input) {
    insurance_plan
    messages
  }
}
```
