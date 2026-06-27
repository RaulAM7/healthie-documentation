---
title: CourseCompletionInfoGroupsType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursecompletioninfogroupstype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursecompletioninfogroupstype/index.md
---

Completion info for group participants enrolled to the course

## Fields

[`completed` ](#field-completed)· [`Int` ](/reference/2026-01-01/scalars/int)· Count of users in the group which completed the course

[`label` ](#field-label)· [`String` ](/reference/2026-01-01/scalars/string)· Group name

[`total` ](#field-total)· [`Int` ](/reference/2026-01-01/scalars/int)· Count of users in the group

[`user_ids` ](#field-user-ids)· [`[String!]` ](/reference/2026-01-01/scalars/string)· Group participant ids

[`value` ](#field-value)· [`String` ](/reference/2026-01-01/scalars/string)· Group ID

## Used By

[`CourseCompletionInfoType.groups`](/reference/2026-01-01/objects/coursecompletioninfotype)

## Definition

```
"""
Completion info for group participants enrolled to the course
"""
type CourseCompletionInfoGroupsType {
  """
  Count of users in the group which completed the course
  """
  completed: Int


  """
  Group name
  """
  label: String


  """
  Count of users in the group
  """
  total: Int


  """
  Group participant ids
  """
  user_ids: [String!]


  """
  Group ID
  """
  value: String
}
```
