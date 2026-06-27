---
title: removeUserFromGroupCarePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/removeuserfromgroupcareplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/removeuserfromgroupcareplan/index.md
---

Remove group care plan user connection for a specific user

## Arguments

[`input` ](#argument-input)· [`removeUserFromGroupCarePlanInput` ](/reference/2026-01-01/input-objects/removeuserfromgroupcareplaninput)· Parameters for removeUserFromGroupCarePlan

## Returns

[`removeUserFromGroupCarePlanPayload`](/reference/2026-01-01/objects/removeuserfromgroupcareplanpayload)

## Example

```
mutation removeUserFromGroupCarePlan($input: removeUserFromGroupCarePlanInput) {
  removeUserFromGroupCarePlan(input: $input) {
    groupCarePlanUserConnection
    messages
  }
}
```
