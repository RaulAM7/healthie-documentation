---
title: AllergySensitivityCategoryType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivitycategorytype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivitycategorytype/index.md
---

Allergy sensitivity category type enum

## Used By

[`AllergySensitivity.category_type`](/reference/2026-01-01/objects/allergysensitivity)

[`createAllergySensitivityInput.category_type`](/reference/2026-01-01/input-objects/createallergysensitivityinput)

[`updateAllergySensitivityInput.category_type`](/reference/2026-01-01/input-objects/updateallergysensitivityinput)

## Definition

```
"""
Allergy sensitivity category type enum
"""
enum AllergySensitivityCategoryType {
  """
  Food
  """
  FOOD


  """
  Drug
  """
  DRUG


  """
  Environmental
  """
  ENVIRONMENTAL


  """
  Pet
  """
  PET


  """
  Latex
  """
  LATEX


  """
  Like
  """
  LIKE


  """
  Dislike
  """
  DISLIKE
}
```
