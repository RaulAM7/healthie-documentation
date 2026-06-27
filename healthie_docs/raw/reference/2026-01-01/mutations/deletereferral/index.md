---
title: deleteReferral | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletereferral/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletereferral/index.md
---

Delete referral

## Arguments

[`input` ](#argument-input)· [`deleteReferralInput` ](/reference/2026-01-01/input-objects/deletereferralinput)· Parameters for deleteReferral

## Returns

[`deleteReferralPayload`](/reference/2026-01-01/objects/deletereferralpayload)

## Example

```
mutation deleteReferral($input: deleteReferralInput) {
  deleteReferral(input: $input) {
    messages
    referral
  }
}
```
