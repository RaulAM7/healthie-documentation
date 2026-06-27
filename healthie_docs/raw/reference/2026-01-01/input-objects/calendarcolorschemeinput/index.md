---
title: CalendarColorSchemeInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/calendarcolorschemeinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/calendarcolorschemeinput/index.md
---

Payload for a calendar color scheme

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the calendar color scheme will be deleted

[`color_code_by` ](#field-color-code-by)· [`String` ](/reference/2026-01-01/scalars/string)· The field, by which the color code is determined. Maximum character limit of 50.

[`color_codes` ](#field-color-codes)· [`[ColorCodeInput]` ](/reference/2026-01-01/input-objects/colorcodeinput)· The color codes of the calendar color scheme

[`default_color` ](#field-default-color)· [`String` ](/reference/2026-01-01/scalars/string)· The default color code. Maximum character limit of 8.

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the calendar color scheme

## Used By

[`createAppointmentSettingInput.calendar_color_schemes`](/reference/2026-01-01/input-objects/createappointmentsettinginput)

[`updateAppointmentSettingInput.calendar_color_schemes`](/reference/2026-01-01/input-objects/updateappointmentsettinginput)

## Definition

```
"""
Payload for a calendar color scheme
"""
input CalendarColorSchemeInput {
  """
  If true, the calendar color scheme will be deleted
  """
  _destroy: Boolean


  """
  The field, by which the color code is determined. Maximum character limit of 50.
  """
  color_code_by: String


  """
  The color codes of the calendar color scheme
  """
  color_codes: [ColorCodeInput]


  """
  The default color code. Maximum character limit of 8.
  """
  default_color: String


  """
  The ID of the calendar color scheme
  """
  id: ID
}
```
