---
title: deleteCustomModule | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustommodule/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustommodule/index.md
---

Destroy an CustomModule

## Arguments

[`input` ](#argument-input)· [`deleteCustomModuleInput` ](/reference/2026-01-01/input-objects/deletecustommoduleinput)· Parameters for deleteCustomModule

## Returns

[`deleteCustomModulePayload`](/reference/2026-01-01/objects/deletecustommodulepayload)

## Example

```
mutation deleteCustomModule($input: deleteCustomModuleInput) {
  deleteCustomModule(input: $input) {
    customModule
    messages
  }
}
```
