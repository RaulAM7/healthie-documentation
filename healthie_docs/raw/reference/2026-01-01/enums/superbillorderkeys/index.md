---
title: SuperBillOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/superbillorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/superbillorderkeys/index.md
---

SuperBill sorting enum

## Used By

[`Query.superBills`](/reference/2026-01-01/queries/superbills)

## Definition

```
"""
SuperBill sorting enum
"""
enum SuperBillOrderKeys {
  NAME_ASC
  NAME_DESC
  SERVICE_DATE_ASC
  SERVICE_DATE_DESC
  AMOUNT_PAID_ASC
  AMOUNT_PAID_DESC
  AMOUNT_BILLED_ASC
  AMOUNT_BILLED_DESC
  STATUS
  CREATED_AT_ASC
  CREATED_AT_DESC
}
```
