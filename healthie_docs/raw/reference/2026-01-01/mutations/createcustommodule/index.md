---
title: createCustomModule | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommodule/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustommodule/index.md
---

create Custom Module

## Arguments

[`input` ](#argument-input)· [`createCustomModuleInput` ](/reference/2026-01-01/input-objects/createcustommoduleinput)· Parameters for createCustomModule

## Returns

[`createCustomModulePayload`](/reference/2026-01-01/objects/createcustommodulepayload)

## Example

```
mutation createCustomModule($input: createCustomModuleInput) {
  createCustomModule(input: $input) {
    customModule
    messages
  }
}
```
