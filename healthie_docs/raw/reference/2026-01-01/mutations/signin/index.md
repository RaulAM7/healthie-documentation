---
title: signIn | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/signin/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/signin/index.md
---

SignIn

## Arguments

[`input` ](#argument-input)· [`signInInput` ](/reference/2026-01-01/input-objects/signininput)· Parameters for signIn

## Returns

[`signInPayload`](/reference/2026-01-01/objects/signinpayload)

## Example

```
mutation signIn($input: signInInput) {
  signIn(input: $input) {
    api_key
    blocked_by_2fa
    blocked_by_2fa_type
    messages
    token
    user
  }
}
```
