---
title: bulkUpdateCarePlanUsers | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkupdatecareplanusers/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkupdatecareplanusers/index.md
---

Trigger notification email or care plan activation for each user related to the selected care plans. In case of activation, a group care plan will be activated for each user of user\_group(unless a user already have an active care plan). If you want to activate selected care plan for only one user(user of group) use ToggleCarePlanStatusForSpecificUser mutation

## Arguments

[`input` ](#argument-input)· [`bulkUpdateCarePlanUsersInput` ](/reference/2026-01-01/input-objects/bulkupdatecareplanusersinput)· Parameters for bulkUpdateCarePlanUsers

## Returns

[`bulkUpdateCarePlanUsersPayload`](/reference/2026-01-01/objects/bulkupdatecareplanuserspayload)

## Example

```
mutation bulkUpdateCarePlanUsers($input: bulkUpdateCarePlanUsersInput) {
  bulkUpdateCarePlanUsers(input: $input) {
    carePlans
    messages
  }
}
```
