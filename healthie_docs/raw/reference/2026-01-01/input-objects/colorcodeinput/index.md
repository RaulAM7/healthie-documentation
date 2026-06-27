---
title: ColorCodeInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/colorcodeinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/colorcodeinput/index.md
---

Payload for a ColorCode

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the color code should be destroyed

[`code_by_item` ](#field-code-by-item)· [`String` ](/reference/2026-01-01/scalars/string)· The code by item of the color code

[`color` ](#field-color)· [`String` ](/reference/2026-01-01/scalars/string)· The color of the color code

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the color code

## Used By

[`CalendarColorSchemeInput.color_codes`](/reference/2026-01-01/input-objects/calendarcolorschemeinput)

## Definition

```
"""
Payload for a ColorCode
"""
input ColorCodeInput {
  """
  If the color code should be destroyed
  """
  _destroy: Boolean


  """
  The code by item of the color code
  """
  code_by_item: String


  """
  The color of the color code
  """
  color: String


  """
  The ID of the color code
  """
  id: ID
}
```
