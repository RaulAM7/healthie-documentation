---
title: updateManualInsurancePayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemanualinsurancepayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemanualinsurancepayment/index.md
---

Update a manual insurance payment

## Arguments

[`input` ](#argument-input)· [`updateManualInsurancePaymentInput` ](/reference/2026-01-01/input-objects/updatemanualinsurancepaymentinput)· Parameters for updateManualInsurancePayment

## Returns

[`updateManualInsurancePaymentPayload`](/reference/2026-01-01/objects/updatemanualinsurancepaymentpayload)

## Example

```
mutation updateManualInsurancePayment(
  $input: updateManualInsurancePaymentInput
) {
  updateManualInsurancePayment(input: $input) {
    insurance_payment
    messages
  }
}
```
