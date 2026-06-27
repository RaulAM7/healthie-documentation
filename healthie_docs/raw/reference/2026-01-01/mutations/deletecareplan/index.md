---
title: deleteCarePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecareplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecareplan/index.md
---

Destroy a Care Plan

## Arguments

[`input` ](#argument-input)· [`deleteCarePlanInput` ](/reference/2026-01-01/input-objects/deletecareplaninput)· Parameters for deleteCarePlan

## Returns

[`deleteCarePlanPayload`](/reference/2026-01-01/objects/deletecareplanpayload)

## Example

```
mutation deleteCarePlan($input: deleteCarePlanInput) {
  deleteCarePlan(input: $input) {
    carePlan
    messages
  }
}
```
