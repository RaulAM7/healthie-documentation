---
title: EraAdjustment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/eraadjustment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/eraadjustment/index.md
---

An adjustment for an ERA service line

## Fields

[`adjustment_group` ](#field-adjustment-group)· [`AdjustmentGroup!` ](/reference/2026-01-01/enums/adjustmentgroup)· required · The adjustment group

[`amount` ](#field-amount)· [`Float!` ](/reference/2026-01-01/scalars/float)· required · The adjustment amount in dollars

[`code` ](#field-code)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The adjustment code

## Used By

[`EraServiceLine.contractual_obligation_adjustments`](/reference/2026-01-01/objects/eraserviceline)

[`EraServiceLine.other_adjustments`](/reference/2026-01-01/objects/eraserviceline)

[`EraServiceLine.patient_responsibility_adjustments`](/reference/2026-01-01/objects/eraserviceline)

[`EraServiceLine.payer_initiated_adjustments`](/reference/2026-01-01/objects/eraserviceline)

## Definition

```
"""
An adjustment for an ERA service line
"""
type EraAdjustment {
  """
  The adjustment group
  """
  adjustment_group: AdjustmentGroup!


  """
  The adjustment amount in dollars
  """
  amount: Float!


  """
  The adjustment code
  """
  code: String!
}
```
