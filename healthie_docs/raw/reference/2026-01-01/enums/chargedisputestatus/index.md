---
title: ChargeDisputeStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/chargedisputestatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/chargedisputestatus/index.md
---

Charge dispute statuses

## Used By

[`ChargeDisputeType.status`](/reference/2026-01-01/objects/chargedisputetype)

## Definition

```
"""
Charge dispute statuses
"""
enum ChargeDisputeStatus {
  LOST
  NEEDS_RESPONSE
  UNDER_REVIEW
  WARNING_CLOSED
  WARNING_NEEDS_RESPONSE
  WARNING_UNDER_REVIEW
  WON
}
```
