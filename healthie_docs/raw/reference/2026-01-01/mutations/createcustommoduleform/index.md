---
title: createCustomModuleForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommoduleform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommoduleform/index.md
---

create Custom Module Form

## Arguments

[`input` ](#argument-input)· [`createCustomModuleFormInput` ](/reference/2026-01-01/input-objects/createcustommoduleforminput)· Parameters for createCustomModuleForm

## Returns

[`createCustomModuleFormPayload`](/reference/2026-01-01/objects/createcustommoduleformpayload)

## Example

```
mutation createCustomModuleForm($input: createCustomModuleFormInput) {
  createCustomModuleForm(input: $input) {
    customModuleForm
    messages
  }
}
```
