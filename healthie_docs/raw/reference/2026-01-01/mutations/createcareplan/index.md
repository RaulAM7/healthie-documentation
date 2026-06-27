---
title: createCarePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcareplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcareplan/index.md
---

Create and return a care plan

## Arguments

[`input` ](#argument-input)· [`createCarePlanInput` ](/reference/2026-01-01/input-objects/createcareplaninput)· Parameters for createCarePlan

## Returns

[`createCarePlanPayload`](/reference/2026-01-01/objects/createcareplanpayload)

## Example

```
mutation createCarePlan($input: createCarePlanInput) {
  createCarePlan(input: $input) {
    carePlan
    messages
  }
}
```
