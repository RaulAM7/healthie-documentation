---
title: deleteRequestedPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleterequestedpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleterequestedpayment/index.md
---

destroy requested payment

## Arguments

[`input` ](#argument-input)· [`deleteRequestedPaymentInput` ](/reference/2026-01-01/input-objects/deleterequestedpaymentinput)· Parameters for deleteRequestedPayment

## Returns

[`deleteRequestedPaymentPayload`](/reference/2026-01-01/objects/deleterequestedpaymentpayload)

## Example

```
mutation deleteRequestedPayment($input: deleteRequestedPaymentInput) {
  deleteRequestedPayment(input: $input) {
    messages
    requested_payment
  }
}
```
