---
title: toggleCarePlanStatusForSpecificUser | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/togglecareplanstatusforspecificuser/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/togglecareplanstatusforspecificuser/index.md
---

Deactivate/activate a group/single Care Plan for a given user

## Arguments

[`input` ](#argument-input)· [`toggleCarePlanStatusForSpecificUserInput` ](/reference/2026-01-01/input-objects/togglecareplanstatusforspecificuserinput)· Parameters for toggleCarePlanStatusForSpecificUser

## Returns

[`toggleCarePlanStatusForSpecificUserPayload`](/reference/2026-01-01/objects/togglecareplanstatusforspecificuserpayload)

## Example

```
mutation toggleCarePlanStatusForSpecificUser(
  $input: toggleCarePlanStatusForSpecificUserInput
) {
  toggleCarePlanStatusForSpecificUser(input: $input) {
    carePlan
    messages
  }
}
```
