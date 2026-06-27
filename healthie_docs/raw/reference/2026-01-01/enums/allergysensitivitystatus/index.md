---
title: AllergySensitivityStatus | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivitystatus/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivitystatus/index.md
---

Allergy sensitivity status enum

## Used By

[`AllergySensitivity.status`](/reference/2026-01-01/objects/allergysensitivity)

[`createAllergySensitivityInput.status`](/reference/2026-01-01/input-objects/createallergysensitivityinput)

[`updateAllergySensitivityInput.status`](/reference/2026-01-01/input-objects/updateallergysensitivityinput)

## Definition

```
"""
Allergy sensitivity status enum
"""
enum AllergySensitivityStatus {
  """
  Active
  """
  ACTIVE


  """
  Inactive
  """
  INACTIVE


  """
  Resolved
  """
  RESOLVED
}
```
