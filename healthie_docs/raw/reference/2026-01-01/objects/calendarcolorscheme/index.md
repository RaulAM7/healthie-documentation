---
title: CalendarColorScheme | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/calendarcolorscheme/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/calendarcolorscheme/index.md
---

A Calendar Color Scheme

## Fields

[`appointment_setting_id` ](#field-appointment-setting-id)· [`String` ](/reference/2026-01-01/scalars/string)· Course ID of benefit

[`color_code_by` ](#field-color-code-by)· [`String` ](/reference/2026-01-01/scalars/string)· The category to color code by

[`color_codes` ](#field-color-codes)· [`[ColorCode!]` ](/reference/2026-01-01/objects/colorcode)· Color code options that make up this color scheme

[`default_color` ](#field-default-color)· [`String` ](/reference/2026-01-01/scalars/string)· The default color (in case the subcategory conditions are not met)

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the scheme

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the connected user

## Used By

[`AppointmentSetting.calendar_color_schemes`](/reference/2026-01-01/objects/appointmentsetting)

## Definition

```
"""
A Calendar Color Scheme
"""
type CalendarColorScheme {
  """
  Course ID of benefit
  """
  appointment_setting_id: String


  """
  The category to color code by
  """
  color_code_by: String


  """
  Color code options that make up this color scheme
  """
  color_codes: [ColorCode!]


  """
  The default color (in case the subcategory conditions are not met)
  """
  default_color: String


  """
  The unique identifier of the scheme
  """
  id: ID!


  """
  The ID of the connected user
  """
  user_id: String
}
```
