---
title: LabOrderOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/laborderorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/laborderorderkeys/index.md
---

LabOrder sorting enum

## Used By

[`Query.labOrders`](/reference/2026-01-01/queries/laborders)

## Definition

```
"""
LabOrder sorting enum
"""
enum LabOrderOrderKeys {
  NAME_ASC
  NAME_DESC
  LAB_ASC
  LAB_DESC
  APPT_ASC
  APPT_DESC
  CLIENT_LAST_NAME_ASC
  CLIENT_LAST_NAME_DESC
  PROVIDER_LAST_NAME_ASC
  PROVIDER_LAST_NAME_DESC
  REVIEWING_PROVIDER_LAST_NAME_ASC
  REVIEWING_PROVIDER_LAST_NAME_DESC
  NORMALIZED_STATUS_ASC
  NORMALIZED_STATUS_DESC
  INTERPRETATION_ASC
  INTERPRETATION_DESC
  UPDATED_AT_ASC
  UPDATED_AT_DESC
}
```
