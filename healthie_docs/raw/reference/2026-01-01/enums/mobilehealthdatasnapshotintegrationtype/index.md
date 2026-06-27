---
title: MobileHealthDataSnapshotIntegrationType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/mobilehealthdatasnapshotintegrationtype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/mobilehealthdatasnapshotintegrationtype/index.md
---

Mobile health data snapshot integration type enum

## Used By

[`CreateMobileHealthDataSnapshotInput.integration_type`](/reference/2026-01-01/input-objects/createmobilehealthdatasnapshotinput)

[`MobileHealthDataSnapshot.integration_type`](/reference/2026-01-01/objects/mobilehealthdatasnapshot)

## Definition

```
"""
Mobile health data snapshot integration type enum
"""
enum MobileHealthDataSnapshotIntegrationType {
  """
  Apple health
  """
  APPLE_HEALTH


  """
  Google health connect
  """
  GOOGLE_HEALTH_CONNECT
}
```
