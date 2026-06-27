---
title: deleteOrganizationMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteorganizationmembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteorganizationmembership/index.md
---

deprecated Organization Memberships Cannot Be Destroyed

Destroy a Organization Membership

## Arguments

[`input` ](#argument-input)· [`deleteOrganizationMembershipInput` ](/reference/2026-01-01/input-objects/deleteorganizationmembershipinput)· Parameters for deleteOrganizationMembership

## Returns

[`deleteOrganizationMembershipPayload`](/reference/2026-01-01/objects/deleteorganizationmembershippayload)

## Example

```
mutation deleteOrganizationMembership(
  $input: deleteOrganizationMembershipInput
) {
  deleteOrganizationMembership(input: $input) {
    messages
    organizationMembership
  }
}
```
