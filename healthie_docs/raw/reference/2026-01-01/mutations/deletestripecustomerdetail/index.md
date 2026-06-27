---
title: deleteStripeCustomerDetail | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletestripecustomerdetail/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletestripecustomerdetail/index.md
---

Deletes a payment card

## Arguments

[`input` ](#argument-input)· [`deleteStripeCustomerDetailInput` ](/reference/2026-01-01/input-objects/deletestripecustomerdetailinput)· Parameters for deleteStripeCustomerDetail

## Returns

[`deleteStripeCustomerDetailPayload`](/reference/2026-01-01/objects/deletestripecustomerdetailpayload)

## Example

```
mutation deleteStripeCustomerDetail($input: deleteStripeCustomerDetailInput) {
  deleteStripeCustomerDetail(input: $input) {
    messages
    stripe_customer_detail
  }
}
```
