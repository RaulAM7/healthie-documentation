---
title: createSetupIntent | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsetupintent/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createsetupintent/index.md
---

Create a Stripe Setup Intent. Used for setting up payment methods for future usage without immediately charging.

## Arguments

[`input` ](#argument-input)· [`createSetupIntentInput` ](/reference/2026-01-01/input-objects/createsetupintentinput)· Parameters for createSetupIntent

## Returns

[`createSetupIntentPayload`](/reference/2026-01-01/objects/createsetupintentpayload)

## Example

```
mutation createSetupIntent($input: createSetupIntentInput) {
  createSetupIntent(input: $input) {
    intentClientSecret
    messages
  }
}
```
