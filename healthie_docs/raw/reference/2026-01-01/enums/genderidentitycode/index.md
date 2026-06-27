---
title: GenderIdentityCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/genderidentitycode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/genderidentitycode/index.md
---

Gender identity code enum

## Used By

[`User.gender_identity_code`](/reference/2026-01-01/objects/user)

[`updateClientInput.gender_identity_code`](/reference/2026-01-01/input-objects/updateclientinput)

[`updateUserInput.gender_identity_code`](/reference/2026-01-01/input-objects/updateuserinput)

## Definition

```
"""
Gender identity code enum
"""
enum GenderIdentityCode {
  """
  Male
  """
  MALE


  """
  Female
  """
  FEMALE


  """
  Female-to-Male (FTM)/Transgender Male/Trans Man
  """
  FEMALE_TO_MALE


  """
  Male-to-Female (MTF)/Transgender Female/Trans Woman
  """
  MALE_TO_FEMALE


  """
  Genderqueer, neither exclusively male nor female
  """
  GENDERQUEER


  """
  Additional gender category or other, please specify
  """
  OTHER


  """
  Choose not to disclose
  """
  CHOOSE_NOT_TO_DISCLOSE
}
```
