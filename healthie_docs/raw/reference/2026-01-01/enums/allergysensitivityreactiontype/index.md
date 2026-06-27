---
title: AllergySensitivityReactionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivityreactiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/allergysensitivityreactiontype/index.md
---

Allergy sensitivity reaction type enum

## Used By

[`AllergySensitivity.reaction_type`](/reference/2026-01-01/objects/allergysensitivity)

[`createAllergySensitivityInput.reaction_type`](/reference/2026-01-01/input-objects/createallergysensitivityinput)

[`updateAllergySensitivityInput.reaction_type`](/reference/2026-01-01/input-objects/updateallergysensitivityinput)

## Definition

```
"""
Allergy sensitivity reaction type enum
"""
enum AllergySensitivityReactionType {
  """
  Allergy
  """
  ALLERGY


  """
  Adverse reaction
  """
  ADVERSE_REACTION
}
```
