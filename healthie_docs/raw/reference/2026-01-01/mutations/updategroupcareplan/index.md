---
title: updateGroupCarePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategroupcareplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategroupcareplan/index.md
---

Updates the care plan status for groups

## Arguments

[`input` ](#argument-input)· [`updateGroupCarePlanInput` ](/reference/2026-01-01/input-objects/updategroupcareplaninput)· Parameters for updateGroupCarePlan

## Returns

[`updateGroupCarePlanPayload`](/reference/2026-01-01/objects/updategroupcareplanpayload)

## Example

```
mutation updateGroupCarePlan($input: updateGroupCarePlanInput) {
  updateGroupCarePlan(input: $input) {
    carePlan
    messages
  }
}
```
