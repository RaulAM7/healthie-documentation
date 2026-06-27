---
title: copyCustomModule | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/copycustommodule/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/copycustommodule/index.md
---

Copy Custom Module

## Arguments

[`input` ](#argument-input)· [`copyCustomModuleInput` ](/reference/2026-01-01/input-objects/copycustommoduleinput)· Parameters for copyCustomModule

## Returns

[`copyCustomModulePayload`](/reference/2026-01-01/objects/copycustommodulepayload)

## Example

```
mutation copyCustomModule($input: copyCustomModuleInput) {
  copyCustomModule(input: $input) {
    customModule
    messages
  }
}
```
