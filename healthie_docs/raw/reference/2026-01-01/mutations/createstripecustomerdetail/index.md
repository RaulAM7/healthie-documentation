---
title: createStripeCustomerDetail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createstripecustomerdetail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createstripecustomerdetail/index.md
---

Creates a new payment card

## Arguments

[`input` ](#argument-input)· [`createStripeCustomerDetailInput` ](/reference/2026-01-01/input-objects/createstripecustomerdetailinput)· Parameters for createStripeCustomerDetail

## Returns

[`createStripeCustomerDetailPayload`](/reference/2026-01-01/objects/createstripecustomerdetailpayload)

## Example

```
mutation createStripeCustomerDetail($input: createStripeCustomerDetailInput) {
  createStripeCustomerDetail(input: $input) {
    messages
    stripeError
    stripe_customer_detail
  }
}
```
