---
title: updateOrganizationCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationcptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateorganizationcptcode/index.md
---

Update a OrganizationCptCode Object

## Arguments

[`input` ](#argument-input)· [`updateOrganizationCptCodeInput` ](/reference/2026-01-01/input-objects/updateorganizationcptcodeinput)· Parameters for updateOrganizationCptCode

## Returns

[`updateOrganizationCptCodePayload`](/reference/2026-01-01/objects/updateorganizationcptcodepayload)

## Example

```
mutation updateOrganizationCptCode($input: updateOrganizationCptCodeInput) {
  updateOrganizationCptCode(input: $input) {
    messages
    organization_cpt_code
  }
}
```
