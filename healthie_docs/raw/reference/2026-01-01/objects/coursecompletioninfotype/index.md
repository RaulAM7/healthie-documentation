---
title: CourseCompletionInfoType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursecompletioninfotype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursecompletioninfotype/index.md
---

Information based on course groups & individuals completion status

## Fields

[`groups` ](#field-groups)· [`[CourseCompletionInfoGroupsType!]` ](/reference/2026-01-01/objects/coursecompletioninfogroupstype)· Complete info for the course user\_groups

[`individuals` ](#field-individuals)· [`[CourseCompletionInfoIndividualsType!]` ](/reference/2026-01-01/objects/coursecompletioninfoindividualstype)· Complete info for the course individual users

## Used By

[`Query.courseCompletetionInfo`](/reference/2026-01-01/queries/coursecompletetioninfo)

[`Query.courseCompletionInfo`](/reference/2026-01-01/queries/coursecompletioninfo)

## Definition

```
"""
Information based on course groups & individuals completion status
"""
type CourseCompletionInfoType {
  """
  Complete info for the course user_groups
  """
  groups: [CourseCompletionInfoGroupsType!]


  """
  Complete info for the course individual users
  """
  individuals: [CourseCompletionInfoIndividualsType!]
}
```
