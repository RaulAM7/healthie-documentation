---
title: CobAdjustmentInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cobadjustmentinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/cobadjustmentinput/index.md
---

A single COB adjustment override (group, reason code, amount)

## Fields

[`adjustment_group` ](#field-adjustment-group)· [`AdjustmentGroup` ](/reference/2026-01-01/enums/adjustmentgroup)· Adjustment group code

[`amount` ](#field-amount)· [`Float` ](/reference/2026-01-01/scalars/float)· Adjustment dollar amount

[`reason_code` ](#field-reason-code)· [`String` ](/reference/2026-01-01/scalars/string)· CARC adjustment reason code

## Used By

[`ClaimLineCobOverridesInput.adjustments`](/reference/2026-01-01/input-objects/claimlinecoboverridesinput)

## Definition

```
"""
A single COB adjustment override (group, reason code, amount)
"""
input CobAdjustmentInput {
  """
  Adjustment group code
  """
  adjustment_group: AdjustmentGroup


  """
  Adjustment dollar amount
  """
  amount: Float


  """
  CARC adjustment reason code
  """
  reason_code: String
}
```
