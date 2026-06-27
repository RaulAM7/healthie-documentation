---
title: updateCarePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecareplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecareplan/index.md
---

Update and return a Care Plan

## Arguments

[`input` ](#argument-input)· [`updateCarePlanInput` ](/reference/2026-01-01/input-objects/updatecareplaninput)· Parameters for updateCarePlan

## Returns

[`updateCarePlanPayload`](/reference/2026-01-01/objects/updatecareplanpayload)

## Example

```
mutation updateCarePlan($input: updateCarePlanInput) {
  updateCarePlan(input: $input) {
    carePlan
    messages
  }
}
```
