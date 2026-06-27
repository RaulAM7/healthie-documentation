---
title: resetPassword | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/resetpassword/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/resetpassword/index.md
---

send the human a password reset email

## Arguments

[`input` ](#argument-input)· [`resetPasswordInput` ](/reference/2026-01-01/input-objects/resetpasswordinput)· Parameters for resetPassword

## Returns

[`resetPasswordPayload`](/reference/2026-01-01/objects/resetpasswordpayload)

## Example

```
mutation resetPassword($input: resetPasswordInput) {
  resetPassword(input: $input) {
    messages
  }
}
```
