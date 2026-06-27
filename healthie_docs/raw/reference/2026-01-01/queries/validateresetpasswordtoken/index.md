---
title: validateResetPasswordToken | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/validateresetpasswordtoken/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/validateresetpasswordtoken/index.md
---

Check if a reset password token is valid

## Arguments

[`token` ](#argument-token)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Boolean`](/reference/2026-01-01/scalars/boolean)

## Example

```
query validateResetPasswordToken($token: String) {
  validateResetPasswordToken(token: $token)
}
```
