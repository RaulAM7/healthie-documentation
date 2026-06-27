---
title: deleteOrganizationCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteorganizationcptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteorganizationcptcode/index.md
---

Delete a OrganizationCptCode Object

## Arguments

[`input` ](#argument-input)· [`deleteOrganizationCptCodeInput` ](/reference/2026-01-01/input-objects/deleteorganizationcptcodeinput)· Parameters for deleteOrganizationCptCode

## Returns

[`deleteOrganizationCptCodePayload`](/reference/2026-01-01/objects/deleteorganizationcptcodepayload)

## Example

```
mutation deleteOrganizationCptCode($input: deleteOrganizationCptCodeInput) {
  deleteOrganizationCptCode(input: $input) {
    messages
    organization_cpt_code
  }
}
```
