---
title: cancelRecurringPayment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/cancelrecurringpayment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/cancelrecurringpayment/index.md
---

Cancels the recurring payment for a patient.

## Arguments

[`input` ](#argument-input)· [`cancelRecurringPaymentInput` ](/reference/2026-01-01/input-objects/cancelrecurringpaymentinput)· Parameters for cancelRecurringPayment

## Returns

[`cancelRecurringPaymentPayload`](/reference/2026-01-01/objects/cancelrecurringpaymentpayload)

## Example

```
mutation cancelRecurringPayment($input: cancelRecurringPaymentInput) {
  cancelRecurringPayment(input: $input) {
    billingItem
    messages
  }
}
```
