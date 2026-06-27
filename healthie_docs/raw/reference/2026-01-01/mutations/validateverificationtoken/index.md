---
title: validateVerificationToken | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/validateverificationtoken/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/validateverificationtoken/index.md
---

Verify 2FA code for Human

## Arguments

[`input` ](#argument-input)· [`validateVerificationTokenInput` ](/reference/2026-01-01/input-objects/validateverificationtokeninput)· Parameters for validateVerificationToken

## Returns

[`validateVerificationTokenPayload`](/reference/2026-01-01/objects/validateverificationtokenpayload)

## Example

```
mutation validateVerificationToken($input: validateVerificationTokenInput) {
  validateVerificationToken(input: $input) {
    messages
    user
  }
}
```
