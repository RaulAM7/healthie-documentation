---
title: updateStripeVerificationDetails | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatestripeverificationdetails/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatestripeverificationdetails/index.md
---

Update Stripe Verification Details

## Arguments

[`input` ](#argument-input)· [`updateStripeVerificationDetailsInput` ](/reference/2026-01-01/input-objects/updatestripeverificationdetailsinput)· Parameters for updateStripeVerificationDetails

## Returns

[`updateStripeVerificationDetailsPayload`](/reference/2026-01-01/objects/updatestripeverificationdetailspayload)

## Example

```
mutation updateStripeVerificationDetails(
  $input: updateStripeVerificationDetailsInput
) {
  updateStripeVerificationDetails(input: $input) {
    messages
    user
  }
}
```
