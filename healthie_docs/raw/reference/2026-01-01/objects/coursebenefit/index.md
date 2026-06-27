---
title: CourseBenefit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/coursebenefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/coursebenefit/index.md
---

A Course Benefit

## Fields

[`benefit` ](#field-benefit)· [`String` ](/reference/2026-01-01/scalars/string)· Benefit of a course

[`course_id` ](#field-course-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Course ID of benefit

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the benefit

## Used By

[`Course.course_benefits`](/reference/2026-01-01/objects/course)

[`createCourseBenefitPayload.courseBenefit`](/reference/2026-01-01/objects/createcoursebenefitpayload)

[`deleteCourseBenefitPayload.courseBenefit`](/reference/2026-01-01/objects/deletecoursebenefitpayload)

## Definition

```
"""
A Course Benefit
"""
type CourseBenefit {
  """
  Benefit of a course
  """
  benefit: String


  """
  Course ID of benefit
  """
  course_id: ID


  """
  The unique identifier of the benefit
  """
  id: ID!
}
```
