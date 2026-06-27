---
title: updateCourseGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecoursegroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecoursegroup/index.md
---

update a Course Group

## Arguments

[`input` ](#argument-input)· [`updateCourseGroupInput` ](/reference/2026-01-01/input-objects/updatecoursegroupinput)· Parameters for updateCourseGroup

## Returns

[`updateCourseGroupPayload`](/reference/2026-01-01/objects/updatecoursegrouppayload)

## Example

```
mutation updateCourseGroup($input: updateCourseGroupInput) {
  updateCourseGroup(input: $input) {
    courseGroup
    messages
  }
}
```
