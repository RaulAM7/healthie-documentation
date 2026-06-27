---
title: asyncBulkCreateOrganizationMemberships | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/asyncbulkcreateorganizationmemberships/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/asyncbulkcreateorganizationmemberships/index.md
---

async bulk create OrganizationMemberships for an organization

## Arguments

[`input` ](#argument-input)· [`asyncBulkCreateOrganizationMembershipsInput` ](/reference/2026-01-01/input-objects/asyncbulkcreateorganizationmembershipsinput)· Parameters for asyncBulkCreateOrganizationMemberships

## Returns

[`asyncBulkCreateOrganizationMembershipsPayload`](/reference/2026-01-01/objects/asyncbulkcreateorganizationmembershipspayload)

## Example

```
mutation asyncBulkCreateOrganizationMemberships(
  $input: asyncBulkCreateOrganizationMembershipsInput
) {
  asyncBulkCreateOrganizationMemberships(input: $input) {
    currentUser
    messages
  }
}
```
