---
title: resetMfa | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/resetmfa/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/resetmfa/index.md
---

Unenrolls the user from multi-factor authentication (MFA), removing their current MFA devices and requiring them to re-enroll if MFA is enforced. Requires permission to edit the target user.

## Arguments

[`input` ](#argument-input)· [`ResetMfaInput` ](/reference/2026-01-01/input-objects/resetmfainput)· Parameters for ResetMfa

## Returns

[`ResetMfaPayload`](/reference/2026-01-01/objects/resetmfapayload)

## Example

```
mutation resetMfa($input: ResetMfaInput) {
  resetMfa(input: $input) {
    messages
  }
}
```
