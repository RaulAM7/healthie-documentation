---
title: createSmartPhrase | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsmartphrase/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsmartphrase/index.md
---

Create a Smart Phrase

## Arguments

[`input` ](#argument-input)· [`createSmartPhraseInput` ](/reference/2026-01-01/input-objects/createsmartphraseinput)· Parameters for createSmartPhrase

## Returns

[`createSmartPhrasePayload`](/reference/2026-01-01/objects/createsmartphrasepayload)

## Example

```
mutation createSmartPhrase($input: createSmartPhraseInput) {
  createSmartPhrase(input: $input) {
    messages
    smartPhrase
  }
}
```
