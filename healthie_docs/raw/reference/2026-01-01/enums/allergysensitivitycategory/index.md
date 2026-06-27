---
title: AllergySensitivityCategory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivitycategory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivitycategory/index.md
---

Allergy sensitivity category enum

## Used By

[`AllergySensitivity.category`](/reference/2026-01-01/objects/allergysensitivity)

[`createAllergySensitivityInput.category`](/reference/2026-01-01/input-objects/createallergysensitivityinput)

[`updateAllergySensitivityInput.category`](/reference/2026-01-01/input-objects/updateallergysensitivityinput)

## Definition

```
"""
Allergy sensitivity category enum
"""
enum AllergySensitivityCategory {
  """
  Allergy
  """
  ALLERGY


  """
  Sensitivity
  """
  SENSITIVITY


  """
  Preference
  """
  PREFERENCE


  """
  Intolerance
  """
  INTOLERANCE


  """
  Ccda
  """
  CCDA
}
```
