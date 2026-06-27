---
title: ColorCodeOption | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/colorcodeoption/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/colorcodeoption/index.md
---

A color code option

## Fields

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· The label of the color code option

[`value` ](#field-value)· [`String` ](/reference/2026-01-01/scalars/string)· The value of the color code option

## Used By

[`Query.colorCodeOptions`](/reference/2026-01-01/queries/colorcodeoptions)

## Definition

```
"""
A color code option
"""
type ColorCodeOption {
  """
  The label of the color code option
  """
  label: String


  """
  The value of the color code option
  """
  value: String
}
```
