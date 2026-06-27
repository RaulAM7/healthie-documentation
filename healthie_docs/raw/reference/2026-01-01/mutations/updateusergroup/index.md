---
title: updateUserGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateusergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateusergroup/index.md
---

Update a Group

## Arguments

[`input` ](#argument-input)· [`updateUserGroupInput` ](/reference/2026-01-01/input-objects/updateusergroupinput)· Parameters for updateUserGroup

## Returns

[`updateUserGroupPayload`](/reference/2026-01-01/objects/updateusergrouppayload)

## Example

```
mutation updateUserGroup($input: updateUserGroupInput) {
  updateUserGroup(input: $input) {
    messages
    user_group
  }
}
```
