---
title: updateUser | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateuser/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateuser/index.md
---

Update the current user, or a patient that the current user has access to. To update other org members, use updateOrganizationMembership

## Arguments

[`input` ](#argument-input)· [`updateUserInput` ](/reference/2026-01-01/input-objects/updateuserinput)· Parameters for updateUser

## Returns

[`updateUserPayload`](/reference/2026-01-01/objects/updateuserpayload)

## Example

```
mutation updateUser($input: updateUserInput) {
  updateUser(input: $input) {
    messages
    user
  }
}
```
