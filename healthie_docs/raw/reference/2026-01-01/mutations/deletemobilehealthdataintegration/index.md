---
title: deleteMobileHealthDataIntegration | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemobilehealthdataintegration/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemobilehealthdataintegration/index.md
---

Destroy Mobile Health Data Integration

## Arguments

[`input` ](#argument-input)· [`DeleteMobileHealthDataIntegrationInput` ](/reference/2026-01-01/input-objects/deletemobilehealthdataintegrationinput)· Parameters for DeleteMobileHealthDataIntegration

## Returns

[`DeleteMobileHealthDataIntegrationPayload`](/reference/2026-01-01/objects/deletemobilehealthdataintegrationpayload)

## Example

```
mutation deleteMobileHealthDataIntegration(
  $input: DeleteMobileHealthDataIntegrationInput
) {
  deleteMobileHealthDataIntegration(input: $input) {
    integration
    messages
  }
}
```
