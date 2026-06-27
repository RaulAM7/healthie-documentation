---
title: deleteCourse | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecourse/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecourse/index.md
---

Destroy a Course

## Arguments

[`input` ](#argument-input)· [`deleteCourseInput` ](/reference/2026-01-01/input-objects/deletecourseinput)· Parameters for deleteCourse

## Returns

[`deleteCoursePayload`](/reference/2026-01-01/objects/deletecoursepayload)

## Example

```
mutation deleteCourse($input: deleteCourseInput) {
  deleteCourse(input: $input) {
    course
    messages
  }
}
```
