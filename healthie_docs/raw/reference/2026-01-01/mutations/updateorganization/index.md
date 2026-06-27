---
title: updateOrganization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganization/index.md
---

Update Organization

## Arguments

[`input` ](#argument-input)· [`updateOrganizationInput` ](/reference/2026-01-01/input-objects/updateorganizationinput)· Parameters for updateOrganization

## Returns

[`updateOrganizationPayload`](/reference/2026-01-01/objects/updateorganizationpayload)

## Example

```
mutation updateOrganization($input: updateOrganizationInput) {
  updateOrganization(input: $input) {
    messages
    organization
    updated_organization_info
  }
}
```
