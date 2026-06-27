---
title: shareCustomModuleForm | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/sharecustommoduleform/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/sharecustommoduleform/index.md
---

share Custom Module Form

## Arguments

[`input` ](#argument-input)· [`shareCustomModuleFormInput` ](/reference/2026-01-01/input-objects/sharecustommoduleforminput)· Parameters for shareCustomModuleForm

## Returns

[`shareCustomModuleFormPayload`](/reference/2026-01-01/objects/sharecustommoduleformpayload)

## Example

```
mutation shareCustomModuleForm($input: shareCustomModuleFormInput) {
  shareCustomModuleForm(input: $input) {
    customModuleForm
    messages
  }
}
```
