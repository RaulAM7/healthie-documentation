---
title: deleteCourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecourseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecourseitem/index.md
---

Destroy a Course Item

## Arguments

[`input` ](#argument-input)· [`deleteCourseItemInput` ](/reference/2026-01-01/input-objects/deletecourseiteminput)· Parameters for deleteCourseItem

## Returns

[`deleteCourseItemPayload`](/reference/2026-01-01/objects/deletecourseitempayload)

## Example

```
mutation deleteCourseItem($input: deleteCourseItemInput) {
  deleteCourseItem(input: $input) {
    courseItem
    messages
  }
}
```
