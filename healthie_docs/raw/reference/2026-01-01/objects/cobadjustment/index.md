---
title: CobAdjustment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cobadjustment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cobadjustment/index.md
---

A single COB adjustment (group, reason code, amount)

## Fields

[`adjustment_group` ](#field-adjustment-group)· [`AdjustmentGroup` ](/reference/2026-01-01/enums/adjustmentgroup)· Adjustment group code (CO, OA, PR, PI)

[`amount` ](#field-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· Adjustment amount

[`reason_code` ](#field-reason-code)· [`String` ](/reference/2026-01-01/scalars/string)· Adjustment reason code

## Used By

[`CobServiceLineAdjustment.adjustments`](/reference/2026-01-01/objects/cobservicelineadjustment)

## Definition

```
"""
A single COB adjustment (group, reason code, amount)
"""
type CobAdjustment {
  """
  Adjustment group code (CO, OA, PR, PI)
  """
  adjustment_group: AdjustmentGroup


  """
  Adjustment amount
  """
  amount: Float


  """
  Adjustment reason code
  """
  reason_code: String
}
```
