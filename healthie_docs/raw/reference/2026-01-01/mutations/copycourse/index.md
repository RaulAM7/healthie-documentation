---
title: copyCourse | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/copycourse/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/copycourse/index.md
---

Copy a Course

## Arguments

[`input` ](#argument-input)· [`copyCourseInput!` ](/reference/2026-01-01/input-objects/copycourseinput)· required · Parameters for copyCourse

## Returns

[`copyCoursePayload`](/reference/2026-01-01/objects/copycoursepayload)

## Example

```
mutation copyCourse($input: copyCourseInput!) {
  copyCourse(input: $input) {
    course
    messages
  }
}
```
