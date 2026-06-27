---
title: copyCustomModuleForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/copycustommoduleform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/copycustommoduleform/index.md
---

copy Custom Module Form

## Arguments

[`input` ](#argument-input)· [`copyCustomModuleFormInput` ](/reference/2026-01-01/input-objects/copycustommoduleforminput)· Parameters for copyCustomModuleForm

## Returns

[`copyCustomModuleFormPayload`](/reference/2026-01-01/objects/copycustommoduleformpayload)

## Example

```
mutation copyCustomModuleForm($input: copyCustomModuleFormInput) {
  copyCustomModuleForm(input: $input) {
    customModuleForm
    messages
  }
}
```
