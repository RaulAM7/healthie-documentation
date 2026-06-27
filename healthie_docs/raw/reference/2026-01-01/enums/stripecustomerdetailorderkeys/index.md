---
title: StripeCustomerDetailOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/stripecustomerdetailorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/stripecustomerdetailorderkeys/index.md
---

StripeCustomerDetails sorting enum

## Used By

[`Query.cardIssues`](/reference/2026-01-01/queries/cardissues)

## Definition

```
"""
StripeCustomerDetails sorting enum
"""
enum StripeCustomerDetailOrderKeys {
  EXPIRATION_DATE_DESC
  EXPIRATION_DATE_ASC
  PATIENT_FIRST_NAME_ASC
  PATIENT_FIRST_NAME_DESC
  CREATED_AT_ASC
  CREATED_AT_DESC
}
```
