---
title: TransferOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/transferorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/transferorderkeys/index.md
---

Transfer sorting enum

## Used By

[`Query.transfers`](/reference/2026-01-01/queries/transfers)

## Definition

```
"""
Transfer sorting enum
"""
enum TransferOrderKeys {
  CREATED_AT_ASC
  CREATED_AT_DESC
  AMOUNT_DESC
  AMOUNT_ASC
  STATUS_DESC
  STATUS_ASC
  EXPECTED_TO_HAPPEN_ASC
  EXPECTED_TO_HAPPEN_DESC
  TRANSACTIONS_COUNT_ASC
  TRANSACTIONS_COUNT_DESC
}
```
