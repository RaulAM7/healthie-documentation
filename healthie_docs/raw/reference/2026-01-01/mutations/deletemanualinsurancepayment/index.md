---
title: deleteManualInsurancePayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemanualinsurancepayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemanualinsurancepayment/index.md
---

Delete a manual insurance payment (soft delete)

## Arguments

[`input` ](#argument-input)· [`deleteManualInsurancePaymentInput` ](/reference/2026-01-01/input-objects/deletemanualinsurancepaymentinput)· Parameters for deleteManualInsurancePayment

## Returns

[`deleteManualInsurancePaymentPayload`](/reference/2026-01-01/objects/deletemanualinsurancepaymentpayload)

## Example

```
mutation deleteManualInsurancePayment(
  $input: deleteManualInsurancePaymentInput
) {
  deleteManualInsurancePayment(input: $input) {
    insurance_payment
    messages
  }
}
```
