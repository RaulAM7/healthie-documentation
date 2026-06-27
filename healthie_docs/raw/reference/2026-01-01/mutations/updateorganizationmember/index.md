---
title: updateOrganizationMember | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationmember/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationmember/index.md
---

Update org members

## Arguments

[`input` ](#argument-input)· [`updateOrganizationMemberInput` ](/reference/2026-01-01/input-objects/updateorganizationmemberinput)· Parameters for updateOrganizationMember

## Returns

[`updateOrganizationMemberPayload`](/reference/2026-01-01/objects/updateorganizationmemberpayload)

## Example

```
mutation updateOrganizationMember($input: updateOrganizationMemberInput) {
  updateOrganizationMember(input: $input) {
    messages
    user
  }
}
```
