---
title: updateReferral | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereferral/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatereferral/index.md
---

Update Referral

## Arguments

[`input` ](#argument-input)· [`updateReferralInput` ](/reference/2026-01-01/input-objects/updatereferralinput)· Parameters for updateReferral

## Returns

[`updateReferralPayload`](/reference/2026-01-01/objects/updatereferralpayload)

## Example

```
mutation updateReferral($input: updateReferralInput) {
  updateReferral(input: $input) {
    messages
    referral
  }
}
```
