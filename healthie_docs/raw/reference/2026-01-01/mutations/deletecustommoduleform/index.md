---
title: deleteCustomModuleForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustommoduleform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustommoduleform/index.md
---

Destroy an CustomModuleForm

## Arguments

[`input` ](#argument-input)· [`deleteCustomModuleFormInput` ](/reference/2026-01-01/input-objects/deletecustommoduleforminput)· Parameters for deleteCustomModuleForm

## Returns

[`deleteCustomModuleFormPayload`](/reference/2026-01-01/objects/deletecustommoduleformpayload)

## Example

```
mutation deleteCustomModuleForm($input: deleteCustomModuleFormInput) {
  deleteCustomModuleForm(input: $input) {
    customModuleForm
    messages
  }
}
```
