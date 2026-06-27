---
title: updateStripeCustomerDetail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatestripecustomerdetail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatestripecustomerdetail/index.md
---

Updates a payment card

## Arguments

[`input` ](#argument-input)· [`updateStripeCustomerDetailInput` ](/reference/2026-01-01/input-objects/updatestripecustomerdetailinput)· Parameters for updateStripeCustomerDetail

## Returns

[`updateStripeCustomerDetailPayload`](/reference/2026-01-01/objects/updatestripecustomerdetailpayload)

## Example

```
mutation updateStripeCustomerDetail($input: updateStripeCustomerDetailInput) {
  updateStripeCustomerDetail(input: $input) {
    messages
    stripe_customer_detail
  }
}
```
