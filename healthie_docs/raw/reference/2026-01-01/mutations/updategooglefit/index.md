---
title: updateGoogleFit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategooglefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updategooglefit/index.md
---

Update GoogleFit

## Arguments

[`input` ](#argument-input)· [`updateGoogleFitInput` ](/reference/2026-01-01/input-objects/updategooglefitinput)· Parameters for updateGoogleFit

## Returns

[`updateGoogleFitPayload`](/reference/2026-01-01/objects/updategooglefitpayload)

## Example

```
mutation updateGoogleFit($input: updateGoogleFitInput) {
  updateGoogleFit(input: $input) {
    google_fit
    messages
  }
}
```
