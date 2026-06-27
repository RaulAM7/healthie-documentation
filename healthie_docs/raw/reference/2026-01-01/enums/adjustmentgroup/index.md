---
title: AdjustmentGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/adjustmentgroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/adjustmentgroup/index.md
---

The type of adjustment group

## Used By

[`CobAdjustment.adjustment_group`](/reference/2026-01-01/objects/cobadjustment)

[`EraAdjustment.adjustment_group`](/reference/2026-01-01/objects/eraadjustment)

[`CobAdjustmentInput.adjustment_group`](/reference/2026-01-01/input-objects/cobadjustmentinput)

## Definition

```
"""
The type of adjustment group
"""
enum AdjustmentGroup {
  """
  Adjustment group for CO
  """
  CO


  """
  Adjustment group for OA
  """
  OA


  """
  Adjustment group for PR
  """
  PR


  """
  Adjustment group for PI
  """
  PI
}
```
