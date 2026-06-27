---
title: deleteSmartPhrase | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesmartphrase/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletesmartphrase/index.md
---

Destroy a Smart Phrase

## Arguments

[`input` ](#argument-input)· [`deleteSmartPhraseInput` ](/reference/2026-01-01/input-objects/deletesmartphraseinput)· Parameters for deleteSmartPhrase

## Returns

[`deleteSmartPhrasePayload`](/reference/2026-01-01/objects/deletesmartphrasepayload)

## Example

```
mutation deleteSmartPhrase($input: deleteSmartPhraseInput) {
  deleteSmartPhrase(input: $input) {
    messages
    smartPhrase
  }
}
```
