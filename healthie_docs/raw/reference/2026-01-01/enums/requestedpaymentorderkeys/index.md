---
title: RequestedPaymentOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/requestedpaymentorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/requestedpaymentorderkeys/index.md
---

RequestedPayment sorting enum

## Used By

[`Query.requestedPayments`](/reference/2026-01-01/queries/requestedpayments)

## Definition

```
"""
RequestedPayment sorting enum
"""
enum RequestedPaymentOrderKeys {
  """
  Sort by client last name and first name ascending
  """
  CLIENT_NAME_ASC


  """
  Sort by client last name and first name descending
  """
  CLIENT_NAME_DESC


  """
  Sort by provider last name and first name ascending
  """
  PROVIDER_NAME_ASC


  """
  Sort by provider last name and first name descending
  """
  PROVIDER_NAME_DESC
  PRICE_ASC
  PRICE_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
  STATUS_ASC
  STATUS_DESC
  TYPE_ASC
  TYPE_DESC
  INVOICE_ID_ASC
  INVOICE_ID_DESC
  WRITE_OFF_AMOUNT_ASC
  WRITE_OFF_AMOUNT_DESC
  BALANCE_DUE_ASC
  BALANCE_DUE_DESC
  SERVICE_DATE_ASC
  SERVICE_DATE_DESC
}
```
