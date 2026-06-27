---
title: deleteCourseGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecoursegroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecoursegroup/index.md
---

Destroy a Course Group

## Arguments

[`input` ](#argument-input)· [`deleteCourseGroupInput` ](/reference/2026-01-01/input-objects/deletecoursegroupinput)· Parameters for deleteCourseGroup

## Returns

[`deleteCourseGroupPayload`](/reference/2026-01-01/objects/deletecoursegrouppayload)

## Example

```
mutation deleteCourseGroup($input: deleteCourseGroupInput) {
  deleteCourseGroup(input: $input) {
    courseGroup
    messages
  }
}
```
