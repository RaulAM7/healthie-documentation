---
title: RaceCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/racecode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/racecode/index.md
---

Race code enum based on OMB standards

## Used By

[`User.primary_race_code`](/reference/2026-01-01/objects/user)

[`User.secondary_race_code`](/reference/2026-01-01/objects/user)

[`updateClientInput.primary_race_code`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateClientInput.secondary_race_code`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateUserInput.primary_race_code`](/reference/2026-01-01/input-objects/updateuserinput)

[`updateUserInput.secondary_race_code`](/reference/2026-01-01/input-objects/updateuserinput)

## Definition

```
"""
Race code enum based on OMB standards
"""
enum RaceCode {
  """
  American Indian or Alaska Native
  """
  AMERICAN_INDIAN_OR_ALASKA_NATIVE


  """
  Asian
  """
  ASIAN


  """
  Black or African American
  """
  BLACK_OR_AFRICAN_AMERICAN


  """
  Native Hawaiian or Other Pacific Islander
  """
  NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER


  """
  Other Race
  """
  OTHER_RACE


  """
  White
  """
  WHITE


  """
  Choose not to disclose
  """
  ASKU
}
```
