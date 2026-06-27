---
title: courseCompletionInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/coursecompletioninfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/coursecompletioninfo/index.md
---

Get course completion info for users and user\_groups

## Arguments

[`course_id` ](#argument-course-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`CourseCompletionInfoType`](/reference/2026-01-01/objects/coursecompletioninfotype)

## Example

```
query courseCompletionInfo($course_id: ID) {
  courseCompletionInfo(course_id: $course_id) {
    groups
    individuals
  }
}
```
