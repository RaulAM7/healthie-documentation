---
title: updateSmartPhrase | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesmartphrase/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatesmartphrase/index.md
---

Update a Smart Phrase

## Arguments

[`input` ](#argument-input)· [`updateSmartPhraseInput` ](/reference/2026-01-01/input-objects/updatesmartphraseinput)· Parameters for updateSmartPhrase

## Returns

[`updateSmartPhrasePayload`](/reference/2026-01-01/objects/updatesmartphrasepayload)

## Example

```
mutation updateSmartPhrase($input: updateSmartPhraseInput) {
  updateSmartPhrase(input: $input) {
    messages
    smartPhrase
  }
}
```
