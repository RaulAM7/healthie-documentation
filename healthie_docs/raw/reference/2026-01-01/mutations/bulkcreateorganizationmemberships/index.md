---
title: bulkCreateOrganizationMemberships | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkcreateorganizationmemberships/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/bulkcreateorganizationmemberships/index.md
---

bulk create OrganizationMemberships for a user

## Arguments

[`input` ](#argument-input)· [`bulkCreateOrganizationMembershipsInput` ](/reference/2026-01-01/input-objects/bulkcreateorganizationmembershipsinput)· Parameters for bulkCreateOrganizationMemberships

## Returns

[`bulkCreateOrganizationMembershipsPayload`](/reference/2026-01-01/objects/bulkcreateorganizationmembershipspayload)

## Example

```
mutation bulkCreateOrganizationMemberships(
  $input: bulkCreateOrganizationMembershipsInput
) {
  bulkCreateOrganizationMemberships(input: $input) {
    currentUser
    messages
    organizationMembership
    other_organization_memberships_count
  }
}
```
