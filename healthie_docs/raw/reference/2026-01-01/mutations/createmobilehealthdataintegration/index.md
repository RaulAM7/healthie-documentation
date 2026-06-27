---
title: createMobileHealthDataIntegration | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmobilehealthdataintegration/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmobilehealthdataintegration/index.md
---

Create Mobile Health Data Integration

## Arguments

[`input` ](#argument-input)· [`CreateMobileHealthDataIntegrationInput` ](/reference/2026-01-01/input-objects/createmobilehealthdataintegrationinput)· Parameters for CreateMobileHealthDataIntegration

## Returns

[`CreateMobileHealthDataIntegrationPayload`](/reference/2026-01-01/objects/createmobilehealthdataintegrationpayload)

## Example

```
mutation createMobileHealthDataIntegration(
  $input: CreateMobileHealthDataIntegrationInput
) {
  createMobileHealthDataIntegration(input: $input) {
    integration
    messages
  }
}
```
