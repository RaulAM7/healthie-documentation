---
title: updateCourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecourseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecourseitem/index.md
---

Update a CourseItem

## Arguments

[`input` ](#argument-input)· [`updateCourseItemInput` ](/reference/2026-01-01/input-objects/updatecourseiteminput)· Parameters for updateCourseItem

## Returns

[`updateCourseItemPayload`](/reference/2026-01-01/objects/updatecourseitempayload)

## Example

```
mutation updateCourseItem($input: updateCourseItemInput) {
  updateCourseItem(input: $input) {
    courseItem
    messages
  }
}
```
