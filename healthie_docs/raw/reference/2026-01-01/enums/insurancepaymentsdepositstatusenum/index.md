---
title: InsurancePaymentsDepositStatusEnum | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/insurancepaymentsdepositstatusenum/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/insurancepaymentsdepositstatusenum/index.md
---

Insurance Payment deposit statuses enum

## Used By

[`InsurancePayment.deposit_status`](/reference/2026-01-01/objects/insurancepayment)

[`Query.insurancePayments`](/reference/2026-01-01/queries/insurancepayments)

[`createInsurancePaymentInput.deposit_status`](/reference/2026-01-01/input-objects/createinsurancepaymentinput)

[`updateInsurancePaymentDepositStatusInput.deposit_status`](/reference/2026-01-01/input-objects/updateinsurancepaymentdepositstatusinput)

[`updateManualInsurancePaymentInput.deposit_status`](/reference/2026-01-01/input-objects/updatemanualinsurancepaymentinput)

## Definition

```
"""
Insurance Payment deposit statuses enum
"""
enum InsurancePaymentsDepositStatusEnum {
  PENDING
  DEPOSITED
}
```
