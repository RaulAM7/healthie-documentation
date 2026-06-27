---
title: validateSignupToken | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/validatesignuptoken/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/validatesignuptoken/index.md
---

Check if a signup token is valid

## Arguments

[`token` ](#argument-token)· [`String`](/reference/2026-01-01/scalars/string)

## Returns

[`Boolean`](/reference/2026-01-01/scalars/boolean)

## Example

```
query validateSignupToken($token: String) {
  validateSignupToken(token: $token)
}
```
