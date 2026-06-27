---
title: InsurancePaymentsOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/insurancepaymentsorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/insurancepaymentsorderkeys/index.md
---

InsurancePayments sorting enum

## Used By

[`Query.insurancePayments`](/reference/2026-01-01/queries/insurancepayments)

## Definition

```
"""
InsurancePayments sorting enum
"""
enum InsurancePaymentsOrderKeys {
  PAID_DATE_DESC
  PAID_DATE_ASC
  PAID_AMOUNT_DESC
  PAID_AMOUNT_ASC
  NPI_DESC
  NPI_ASC
  SOURCE_DESC
  SOURCE_ASC
  PAYER_NAME_DESC
  PAYER_NAME_ASC
  ACH_CHECK_NUMBER_DESC
  ACH_CHECK_NUMBER_ASC
  CREATED_AT_DESC
  CREATED_AT_ASC
  UPDATED_AT_DESC
  UPDATED_AT_ASC
}
```
