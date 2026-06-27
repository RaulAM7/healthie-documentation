---
title: createRequestedPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrequestedpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrequestedpayment/index.md
---

create requested payment

## Arguments

[`input` ](#argument-input)· [`createRequestedPaymentInput` ](/reference/2026-01-01/input-objects/createrequestedpaymentinput)· Parameters for createRequestedPayment

## Returns

[`createRequestedPaymentPayload`](/reference/2026-01-01/objects/createrequestedpaymentpayload)

## Example

```
mutation createRequestedPayment($input: createRequestedPaymentInput) {
  createRequestedPayment(input: $input) {
    messages
    requestedPayment
  }
}
```
