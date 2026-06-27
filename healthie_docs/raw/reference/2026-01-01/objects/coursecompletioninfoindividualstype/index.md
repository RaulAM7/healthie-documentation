---
title: CourseCompletionInfoIndividualsType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursecompletioninfoindividualstype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursecompletioninfoindividualstype/index.md
---

Completion info for individual participants enrolled to the course

## Fields

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· User full\_name

[`value` ](#field-value)· [`String` ](/reference/2026-01-01/scalars/string)· User ID

## Used By

[`CourseCompletionInfoType.individuals`](/reference/2026-01-01/objects/coursecompletioninfotype)

## Definition

```
"""
Completion info for individual participants enrolled to the course
"""
type CourseCompletionInfoIndividualsType {
  """
  User full_name
  """
  label: String


  """
  User ID
  """
  value: String
}
```
