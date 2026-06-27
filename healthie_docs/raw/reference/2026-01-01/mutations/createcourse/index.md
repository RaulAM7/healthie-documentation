---
title: createCourse | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcourse/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcourse/index.md
---

create Course

## Arguments

[`input` ](#argument-input)· [`createCourseInput` ](/reference/2026-01-01/input-objects/createcourseinput)· Parameters for createCourse

## Returns

[`createCoursePayload`](/reference/2026-01-01/objects/createcoursepayload)

## Example

```
mutation createCourse($input: createCourseInput) {
  createCourse(input: $input) {
    course
    messages
  }
}
```
