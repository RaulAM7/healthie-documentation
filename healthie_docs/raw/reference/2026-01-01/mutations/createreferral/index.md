---
title: createReferral | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createreferral/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createreferral/index.md
---

Create new Referring Physician

## Arguments

[`input` ](#argument-input)· [`createReferralInput` ](/reference/2026-01-01/input-objects/createreferralinput)· Parameters for createReferral

## Returns

[`createReferralPayload`](/reference/2026-01-01/objects/createreferralpayload)

## Example

```
mutation createReferral($input: createReferralInput) {
  createReferral(input: $input) {
    messages
    referral
  }
}
```
