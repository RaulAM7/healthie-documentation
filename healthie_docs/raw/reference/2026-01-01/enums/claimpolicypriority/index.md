---
title: ClaimPolicyPriority | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/claimpolicypriority/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/claimpolicypriority/index.md
---

Insurance policy priority level

## Used By

[`ClaimPolicy.priority_type`](/reference/2026-01-01/objects/claimpolicy)

## Definition

```
"""
Insurance policy priority level
"""
enum ClaimPolicyPriority {
  """
  Primary insurance
  """
  PRIMARY


  """
  Secondary insurance
  """
  SECONDARY


  """
  Inactive policy
  """
  INACTIVE


  """
  Carve-out insurance
  """
  CARVE_OUT
}
```
