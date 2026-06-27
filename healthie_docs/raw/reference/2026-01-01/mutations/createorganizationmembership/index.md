---
title: createOrganizationMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createorganizationmembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createorganizationmembership/index.md
---

create OrganizationMembership

## Arguments

[`input` ](#argument-input)· [`createOrganizationMembershipInput` ](/reference/2026-01-01/input-objects/createorganizationmembershipinput)· Parameters for createOrganizationMembership

## Returns

[`createOrganizationMembershipPayload`](/reference/2026-01-01/objects/createorganizationmembershippayload)

## Example

```
mutation createOrganizationMembership(
  $input: createOrganizationMembershipInput
) {
  createOrganizationMembership(input: $input) {
    currentUser
    messages
    organizationMembership
  }
}
```
