---
title: createPaymentIntent | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpaymentintent/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createpaymentintent/index.md
---

Create a Stripe Payment Intent. Currently used for supporting additional payment methods via a custom front-end. When the payment succeeds, Healthie will receive a webhook and automatically complete the checkout.

## Arguments

[`input` ](#argument-input)· [`createPaymentIntentInput` ](/reference/2026-01-01/input-objects/createpaymentintentinput)· Parameters for createPaymentIntent

## Returns

[`createPaymentIntentPayload`](/reference/2026-01-01/objects/createpaymentintentpayload)

## Example

```
mutation createPaymentIntent($input: createPaymentIntentInput) {
  createPaymentIntent(input: $input) {
    intentClientSecret
    messages
  }
}
```
