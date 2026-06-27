---
title: createProviderCptCodes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createprovidercptcodes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createprovidercptcodes/index.md
---

Create ProviderCPTCode Objects

## Arguments

[`input` ](#argument-input)· [`createProviderCptCodesInput` ](/reference/2026-01-01/input-objects/createprovidercptcodesinput)· Parameters for createProviderCptCodes

## Returns

[`createProviderCptCodesPayload`](/reference/2026-01-01/objects/createprovidercptcodespayload)

## Example

```
mutation createProviderCptCodes($input: createProviderCptCodesInput) {
  createProviderCptCodes(input: $input) {
    messages
  }
}
```
