---
title: updateRequestedPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updaterequestedpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updaterequestedpayment/index.md
---

update requested payment

## Arguments

[`input` ](#argument-input)· [`updateRequestedPaymentInput` ](/reference/2026-01-01/input-objects/updaterequestedpaymentinput)· Parameters for updateRequestedPayment

## Returns

[`updateRequestedPaymentPayload`](/reference/2026-01-01/objects/updaterequestedpaymentpayload)

## Example

```
mutation updateRequestedPayment($input: updateRequestedPaymentInput) {
  updateRequestedPayment(input: $input) {
    messages
    requested_payment
  }
}
```
