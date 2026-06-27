---
title: createInsurancePayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinsurancepayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createinsurancepayment/index.md
---

Create a manual insurance payment

## Arguments

[`input` ](#argument-input)· [`createInsurancePaymentInput` ](/reference/2026-01-01/input-objects/createinsurancepaymentinput)· Parameters for createInsurancePayment

## Returns

[`createInsurancePaymentPayload`](/reference/2026-01-01/objects/createinsurancepaymentpayload)

## Example

```
mutation createInsurancePayment($input: createInsurancePaymentInput) {
  createInsurancePayment(input: $input) {
    insurance_payment
    messages
  }
}
```
