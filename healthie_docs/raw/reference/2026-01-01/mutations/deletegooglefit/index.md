---
title: deleteGoogleFit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletegooglefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletegooglefit/index.md
---

Destroy GoogleFit

## Arguments

[`input` ](#argument-input)· [`deleteGoogleFitInput` ](/reference/2026-01-01/input-objects/deletegooglefitinput)· Parameters for deleteGoogleFit

## Returns

[`deleteGoogleFitPayload`](/reference/2026-01-01/objects/deletegooglefitpayload)

## Example

```
mutation deleteGoogleFit($input: deleteGoogleFitInput) {
  deleteGoogleFit(input: $input) {
    google_fit
    messages
  }
}
```
