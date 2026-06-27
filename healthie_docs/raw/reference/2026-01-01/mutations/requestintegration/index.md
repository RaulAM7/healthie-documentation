---
title: requestIntegration | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/requestintegration/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/requestintegration/index.md
---

Send an email asking support to enable a given integration.

## Arguments

[`input` ](#argument-input)· [`RequestIntegrationInput` ](/reference/2026-01-01/input-objects/requestintegrationinput)· Parameters for RequestIntegration

## Returns

[`RequestIntegrationPayload`](/reference/2026-01-01/objects/requestintegrationpayload)

## Example

```
mutation requestIntegration($input: RequestIntegrationInput) {
  requestIntegration(input: $input) {
    messages
    success_string
  }
}
```
