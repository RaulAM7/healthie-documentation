---
title: updateCustomModuleForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustommoduleform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustommoduleform/index.md
---

Update an Custom Module Form and return Custom Module Form

## Arguments

[`input` ](#argument-input)· [`updateCustomModuleFormInput` ](/reference/2026-01-01/input-objects/updatecustommoduleforminput)· Parameters for updateCustomModuleForm

## Returns

[`updateCustomModuleFormPayload`](/reference/2026-01-01/objects/updatecustommoduleformpayload)

## Example

```
mutation updateCustomModuleForm($input: updateCustomModuleFormInput) {
  updateCustomModuleForm(input: $input) {
    customModuleForm
    messages
  }
}
```
