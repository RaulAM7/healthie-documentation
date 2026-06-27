---
title: LabOrderInterpretation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/laborderinterpretation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/laborderinterpretation/index.md
---

Interpretations for Lab Orders and related objects

## Used By

[`LabObservationResult.interpretation`](/reference/2026-01-01/objects/labobservationresult)

[`LabOrder.interpretation`](/reference/2026-01-01/objects/laborder)

[`LabResult.interpretation`](/reference/2026-01-01/objects/labresult)

## Definition

```
"""
Interpretations for Lab Orders and related objects
"""
enum LabOrderInterpretation {
  """
  Unknown interpretation
  """
  UNKNOWN


  """
  Normal
  """
  NORMAL


  """
  Abnormal
  """
  ABNORMAL


  """
  Critical
  """
  CRITICAL
}
```
