---
title: MobileHealthDataSnapshotStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/mobilehealthdatasnapshotstatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/mobilehealthdatasnapshotstatus/index.md
---

Mobile health data snapshot status enum

## Used By

[`MobileHealthDataSnapshot.current_status`](/reference/2026-01-01/objects/mobilehealthdatasnapshot)

## Definition

```
"""
Mobile health data snapshot status enum
"""
enum MobileHealthDataSnapshotStatus {
  """
  Initialized
  """
  INITIALIZED


  """
  Processing
  """
  PROCESSING


  """
  Partially processed
  """
  PARTIALLY_PROCESSED


  """
  Processed
  """
  PROCESSED


  """
  Failed
  """
  FAILED
}
```
