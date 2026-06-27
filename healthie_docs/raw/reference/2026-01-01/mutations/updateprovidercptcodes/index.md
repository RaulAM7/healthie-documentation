---
title: updateProviderCptCodes | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateprovidercptcodes/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateprovidercptcodes/index.md
---

Update ProviderCptCode Objects

## Arguments

[`input` ](#argument-input)· [`updateProviderCptCodesInput` ](/reference/2026-01-01/input-objects/updateprovidercptcodesinput)· Parameters for updateProviderCptCodes

## Returns

[`updateProviderCptCodesPayload`](/reference/2026-01-01/objects/updateprovidercptcodespayload)

## Example

```
mutation updateProviderCptCodes($input: updateProviderCptCodesInput) {
  updateProviderCptCodes(input: $input) {
    messages
  }
}
```
