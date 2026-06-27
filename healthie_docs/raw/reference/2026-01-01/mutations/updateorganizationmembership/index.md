---
title: updateOrganizationMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationmembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationmembership/index.md
---

Update a OrganizationMembership

## Arguments

[`input` ](#argument-input)· [`updateOrganizationMembershipInput` ](/reference/2026-01-01/input-objects/updateorganizationmembershipinput)· Parameters for updateOrganizationMembership

## Returns

[`updateOrganizationMembershipPayload`](/reference/2026-01-01/objects/updateorganizationmembershippayload)

## Example

```
mutation updateOrganizationMembership(
  $input: updateOrganizationMembershipInput
) {
  updateOrganizationMembership(input: $input) {
    messages
    organizationMembership
  }
}
```
