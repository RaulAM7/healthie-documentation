---
title: BillingItemOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/billingitemorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/billingitemorderkeys/index.md
---

BillingItem sorting enum

## Used By

[`Query.billingItems`](/reference/2026-01-01/queries/billingitems)

## Definition

```
"""
BillingItem sorting enum
"""
enum BillingItemOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
  AMOUNT_PAID_DESC
  AMOUNT_PAID_ASC
  PATIENT_FIRST_NAME_ASC
  PATIENT_FIRST_NAME_DESC
  PROVIDER_FIRST_NAME_ASC
  PROVIDER_FIRST_NAME_DESC


  """
  Sort by the payment medium ascending
  """
  METHOD_ASC


  """
  Sort by the payment medium descending
  """
  METHOD_DESC
  STATE_ASC
  STATE_DESC
}
```
