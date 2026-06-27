---
title: HolderRelationship | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/holderrelationship/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/holderrelationship/index.md
---

Relationship of the insurance subscriber to the patient

## Used By

[`ClaimPolicyHolder.relationship`](/reference/2026-01-01/objects/claimpolicyholder)

## Definition

```
"""
Relationship of the insurance subscriber to the patient
"""
enum HolderRelationship {
  """
  Patient is the subscriber
  """
  SELF


  """
  Patient is the child of the subscriber
  """
  CHILD


  """
  Patient is the spouse of the subscriber
  """
  SPOUSE


  """
  No relationship specified
  """
  NONE


  """
  Other relationship
  """
  OTHER
}
```
