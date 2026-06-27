---
title: ContactTypeOverrideInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/contacttypeoverrideinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/contacttypeoverrideinput/index.md
---

Payload for overriding a contact type

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the contact type override

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the contact type. Maximum character limit of 25.

[`position` ](#field-position)· [`Int` ](/reference/2026-01-01/scalars/int)· The position of the contact type

[`show` ](#field-show)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not to show the contact type

## Used By

[`createAppointmentSettingInput.contact_type_overrides`](/reference/2026-01-01/input-objects/createappointmentsettinginput)

[`updateAppointmentSettingInput.contact_type_overrides`](/reference/2026-01-01/input-objects/updateappointmentsettinginput)

## Definition

```
"""
Payload for overriding a contact type
"""
input ContactTypeOverrideInput {
  """
  The ID of the contact type override
  """
  id: ID


  """
  The name of the contact type. Maximum character limit of 25.
  """
  name: String


  """
  The position of the contact type
  """
  position: Int


  """
  Whether or not to show the contact type
  """
  show: Boolean
}
```
