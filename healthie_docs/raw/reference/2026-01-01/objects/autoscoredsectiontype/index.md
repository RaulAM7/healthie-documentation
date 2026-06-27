---
title: AutoscoredSectionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/autoscoredsectiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/autoscoredsectiontype/index.md
---

The autoscored section for a filled form

## Fields

[`has_autoscored_calculator` ](#field-has-autoscored-calculator)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· The autoscored section has a live autoscoring module(mod\_type: "autoscored\_calculator") if true.

[`section_key` ](#field-section-key)· [`String` ](/reference/2026-01-01/scalars/string)· The key of the section

[`section_title` ](#field-section-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title of the section

[`show` ](#field-show)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Is false when none of the questions for the autoscored section are answered

[`value` ](#field-value)· [`Float` ](/reference/2026-01-01/scalars/float)· The value of the section

## Used By

[`FormAnswerGroup.autoscored_sections`](/reference/2026-01-01/objects/formanswergroup)

## Definition

```
"""
The autoscored section for a filled form
"""
type AutoscoredSectionType {
  """
  The autoscored section has a live autoscoring module(mod_type: "autoscored_calculator") if true.
  """
  has_autoscored_calculator: Boolean


  """
  The key of the section
  """
  section_key: String


  """
  The title of the section
  """
  section_title: String


  """
  Is false when none of the questions for the autoscored section are answered
  """
  show: Boolean


  """
  The value of the section
  """
  value: Float
}
```
