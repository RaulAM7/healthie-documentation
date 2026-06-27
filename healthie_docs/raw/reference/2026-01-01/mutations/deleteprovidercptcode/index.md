---
title: deleteProviderCptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteprovidercptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteprovidercptcode/index.md
---

Delete a ProviderCptCode Object

## Arguments

[`input` ](#argument-input)· [`deleteProviderCptCodeInput` ](/reference/2026-01-01/input-objects/deleteprovidercptcodeinput)· Parameters for deleteProviderCptCode

## Returns

[`deleteProviderCptCodePayload`](/reference/2026-01-01/objects/deleteprovidercptcodepayload)

## Example

```
mutation deleteProviderCptCode($input: deleteProviderCptCodeInput) {
  deleteProviderCptCode(input: $input) {
    messages
    provider_cpt_code
  }
}
```
