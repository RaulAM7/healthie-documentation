---
title: EthnicityCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/ethnicitycode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/ethnicitycode/index.md
---

Ethnicity code enum based on OMB standards

## Used By

[`User.primary_ethnicity_code`](/reference/2026-01-01/objects/user)

[`User.secondary_ethnicity_code`](/reference/2026-01-01/objects/user)

[`updateClientInput.primary_ethnicity_code`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateClientInput.secondary_ethnicity_code`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateUserInput.primary_ethnicity_code`](/reference/2026-01-01/input-objects/updateuserinput)

[`updateUserInput.secondary_ethnicity_code`](/reference/2026-01-01/input-objects/updateuserinput)

## Definition

```
"""
Ethnicity code enum based on OMB standards
"""
enum EthnicityCode {
  """
  Hispanic or Latino
  """
  HISPANIC_OR_LATINO


  """
  Not Hispanic or Latino
  """
  NOT_HISPANIC_OR_LATINO


  """
  Choose not to disclose
  """
  ASKU
}
```
