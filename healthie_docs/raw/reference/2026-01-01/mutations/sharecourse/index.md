---
title: shareCourse | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/sharecourse/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/sharecourse/index.md
---

share Course with another provider

## Arguments

[`input` ](#argument-input)· [`shareCourseInput` ](/reference/2026-01-01/input-objects/sharecourseinput)· Parameters for shareCourse

## Returns

[`shareCoursePayload`](/reference/2026-01-01/objects/sharecoursepayload)

## Example

```
mutation shareCourse($input: shareCourseInput) {
  shareCourse(input: $input) {
    course
    messages
  }
}
```
