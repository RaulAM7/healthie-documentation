---
title: signUp | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/signup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/signup/index.md
---

Sign up

## Arguments

[`input` ](#argument-input)· [`signUpInput` ](/reference/2026-01-01/input-objects/signupinput)· Parameters for signUp

## Returns

[`signUpPayload`](/reference/2026-01-01/objects/signuppayload)

## Example

```
mutation signUp($input: signUpInput) {
  signUp(input: $input) {
    initialMessage
    messages
    nextRequiredStep
    token
    user
    whitelabelSetting
  }
}
```
