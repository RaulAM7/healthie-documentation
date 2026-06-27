---
title: createGoogleFit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategooglefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/creategooglefit/index.md
---

Create GoogleFit

## Arguments

[`input` ](#argument-input)· [`createGoogleFitInput` ](/reference/2026-01-01/input-objects/creategooglefitinput)· Parameters for createGoogleFit

## Returns

[`createGoogleFitPayload`](/reference/2026-01-01/objects/creategooglefitpayload)

## Example

```
mutation createGoogleFit($input: createGoogleFitInput) {
  createGoogleFit(input: $input) {
    google_fit
    messages
  }
}
```
