---
title: updateCustomModule | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustommodule/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustommodule/index.md
---

Update an Custom Module and return Custom Module

## Arguments

[`input` ](#argument-input)· [`updateCustomModuleInput` ](/reference/2026-01-01/input-objects/updatecustommoduleinput)· Parameters for updateCustomModule

## Returns

[`updateCustomModulePayload`](/reference/2026-01-01/objects/updatecustommodulepayload)

## Example

```
mutation updateCustomModule($input: updateCustomModuleInput) {
  updateCustomModule(input: $input) {
    customModule
    messages
  }
}
```
