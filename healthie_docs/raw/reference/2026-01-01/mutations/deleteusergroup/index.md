---
title: deleteUserGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteusergroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteusergroup/index.md
---

Delete a Group

## Arguments

[`input` ](#argument-input)· [`deleteUserGroupInput` ](/reference/2026-01-01/input-objects/deleteusergroupinput)· Parameters for deleteUserGroup

## Returns

[`deleteUserGroupPayload`](/reference/2026-01-01/objects/deleteusergrouppayload)

## Example

```
mutation deleteUserGroup($input: deleteUserGroupInput) {
  deleteUserGroup(input: $input) {
    messages
    user_group
  }
}
```
