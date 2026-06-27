---
title: courseCompletetionInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/coursecompletetioninfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/coursecompletetioninfo/index.md
---

deprecated Use \`course\_completion\_info\` instead

Get course completion info for users and user\_groups

## Arguments

[`course_id` ](#argument-course-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`CourseCompletionInfoType`](/reference/2026-01-01/objects/coursecompletioninfotype)

## Example

```
query courseCompletetionInfo($course_id: ID) {
  courseCompletetionInfo(course_id: $course_id) {
    groups
    individuals
  }
}
```
