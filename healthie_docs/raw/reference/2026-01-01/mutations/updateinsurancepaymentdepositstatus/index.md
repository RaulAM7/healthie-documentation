---
title: updateInsurancePaymentDepositStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinsurancepaymentdepositstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateinsurancepaymentdepositstatus/index.md
---

Update the deposit status of an insurance payment

## Arguments

[`input` ](#argument-input)· [`updateInsurancePaymentDepositStatusInput` ](/reference/2026-01-01/input-objects/updateinsurancepaymentdepositstatusinput)· Parameters for updateInsurancePaymentDepositStatus

## Returns

[`updateInsurancePaymentDepositStatusPayload`](/reference/2026-01-01/objects/updateinsurancepaymentdepositstatuspayload)

## Example

```
mutation updateInsurancePaymentDepositStatus(
  $input: updateInsurancePaymentDepositStatusInput
) {
  updateInsurancePaymentDepositStatus(input: $input) {
    insurance_payment
    messages
  }
}
```
