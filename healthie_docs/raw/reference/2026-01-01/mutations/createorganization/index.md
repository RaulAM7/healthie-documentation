---
title: createOrganization | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createorganization/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createorganization/index.md
---

create Organization

## Arguments

[`input` ](#argument-input)· [`createOrganizationInput` ](/reference/2026-01-01/input-objects/createorganizationinput)· Parameters for createOrganization

## Returns

[`createOrganizationPayload`](/reference/2026-01-01/objects/createorganizationpayload)

## Example

```
mutation createOrganization($input: createOrganizationInput) {
  createOrganization(input: $input) {
    currentUser
    messages
    organization
  }
}
```
