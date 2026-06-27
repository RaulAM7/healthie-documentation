---
title: createOrganizationCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createorganizationcptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createorganizationcptcode/index.md
---

Create an Organization CPT Code Object

## Arguments

[`input` ](#argument-input)· [`createOrganizationCptCodeInput` ](/reference/2026-01-01/input-objects/createorganizationcptcodeinput)· Parameters for createOrganizationCptCode

## Returns

[`createOrganizationCptCodePayload`](/reference/2026-01-01/objects/createorganizationcptcodepayload)

## Example

```
mutation createOrganizationCptCode($input: createOrganizationCptCodeInput) {
  createOrganizationCptCode(input: $input) {
    messages
    organization_cpt_code
  }
}
```
