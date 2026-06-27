---
title: OtherIdNumberInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/otheridnumberinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/otheridnumberinput/index.md
---

Payload for another id number

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the other id number

[`other_id` ](#field-other-id)· [`String` ](/reference/2026-01-01/scalars/string)· The other id number

[`other_id_qualifier` ](#field-other-id-qualifier)· [`String` ](/reference/2026-01-01/scalars/string)· The qualifier of the other id number

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The user ID of the other id number

## Used By

[`createCms1500Input.rendering_provider_other_id_number`](/reference/2026-01-01/input-objects/createcms1500input)

[`updateCms1500Input.rendering_provider_other_id_number`](/reference/2026-01-01/input-objects/updatecms1500input)

## Definition

```
"""
Payload for another id number
"""
input OtherIdNumberInput {
  """
  The ID of the other id number
  """
  id: ID


  """
  The other id number
  """
  other_id: String


  """
  The qualifier of the other id number
  """
  other_id_qualifier: String


  """
  The user ID of the other id number
  """
  user_id: String
}
```
