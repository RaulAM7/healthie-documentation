---
title: revokeToken | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/revoketoken/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/revoketoken/index.md
---

revoke token or API key.

## Arguments

[`input` ](#argument-input)· [`revokeTokenInput` ](/reference/2026-01-01/input-objects/revoketokeninput)· Parameters for revokeToken

## Returns

[`revokeTokenPayload`](/reference/2026-01-01/objects/revoketokenpayload)

## Example

```
mutation revokeToken($input: revokeTokenInput) {
  revokeToken(input: $input) {
    messages
  }
}
```
