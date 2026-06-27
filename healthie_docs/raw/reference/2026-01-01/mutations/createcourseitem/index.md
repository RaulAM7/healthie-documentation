---
title: createCourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcourseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcourseitem/index.md
---

create CourseItem

## Arguments

[`input` ](#argument-input)· [`createCourseItemInput` ](/reference/2026-01-01/input-objects/createcourseiteminput)· Parameters for createCourseItem

## Returns

[`createCourseItemPayload`](/reference/2026-01-01/objects/createcourseitempayload)

## Example

```
mutation createCourseItem($input: createCourseItemInput) {
  createCourseItem(input: $input) {
    courseItem
    messages
    redirect_url
  }
}
```
