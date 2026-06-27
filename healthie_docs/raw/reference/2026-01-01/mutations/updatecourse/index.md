---
title: updateCourse | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecourse/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecourse/index.md
---

Update a Course

## Arguments

[`input` ](#argument-input)· [`updateCourseInput` ](/reference/2026-01-01/input-objects/updatecourseinput)· Parameters for updateCourse

## Returns

[`updateCoursePayload`](/reference/2026-01-01/objects/updatecoursepayload)

## Example

```
mutation updateCourse($input: updateCourseInput) {
  updateCourse(input: $input) {
    course
    messages
  }
}
```
