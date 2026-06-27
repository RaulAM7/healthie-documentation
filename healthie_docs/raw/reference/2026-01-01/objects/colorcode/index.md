---
title: ColorCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/colorcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/colorcode/index.md
---

A Calendar Color Scheme

## Fields

[`calendar_color_scheme_id` ](#field-calendar-color-scheme-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the calendar color scheme

[`code_by_item` ](#field-code-by-item)· [`String` ](/reference/2026-01-01/scalars/string)· The item to code by

[`code_by_item_name` ](#field-code-by-item-name)· [`String` ](/reference/2026-01-01/scalars/string)· The item name to code by

[`color` ](#field-color)· [`String` ](/reference/2026-01-01/scalars/string)· The color

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the color code

## Used By

[`CalendarColorScheme.color_codes`](/reference/2026-01-01/objects/calendarcolorscheme)

## Definition

```
"""
A Calendar Color Scheme
"""
type ColorCode {
  """
  The ID of the calendar color scheme
  """
  calendar_color_scheme_id: String


  """
  The item to code by
  """
  code_by_item: String


  """
  The item name to code by
  """
  code_by_item_name: String


  """
  The color
  """
  color: String


  """
  The unique identifier of the color code
  """
  id: ID!
}
```
