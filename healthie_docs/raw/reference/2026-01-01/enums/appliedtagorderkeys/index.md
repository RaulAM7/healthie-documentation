---
title: AppliedTagOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/appliedtagorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/appliedtagorderkeys/index.md
---

AppliedTag sorting enum

## Used By

[`Query.appliedTags`](/reference/2026-01-01/queries/appliedtags)

## Definition

```
"""
AppliedTag sorting enum
"""
enum AppliedTagOrderKeys {
  """
  Sort by created at in ascending order
  """
  CREATED_AT_ASC


  """
  Sort by created at in descending order
  """
  CREATED_AT_DESC


  """
  Sort by updated at in ascending order
  """
  UPDATED_AT_ASC


  """
  Sort by updated at in descending order
  """
  UPDATED_AT_DESC


  """
  Do not sort records
  """
  UNSORTED
}
```
