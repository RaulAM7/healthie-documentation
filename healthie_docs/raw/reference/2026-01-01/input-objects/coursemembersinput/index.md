---
title: CourseMembersInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/coursemembersinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/coursemembersinput/index.md
---

Course members input as a label-value pair

## Fields

[`label` ](#field-label)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Label for the value

[`value` ](#field-value)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Value for the label

## Used By

[`updateCourseInput.course_members`](/reference/2026-01-01/input-objects/updatecourseinput)

## Definition

```
"""
Course members input as a label-value pair
"""
input CourseMembersInput {
  """
  Label for the value
  """
  label: String!


  """
  Value for the label
  """
  value: String!
}
```
