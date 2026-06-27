---
title: createCompletedCourseItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcompletedcourseitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcompletedcourseitem/index.md
---

create CompletedCourseItem

## Arguments

[`input` ](#argument-input)· [`createCompletedCourseItemInput!` ](/reference/2026-01-01/input-objects/createcompletedcourseiteminput)· required · Parameters for createCompletedCourseItem

## Returns

[`createCompletedCourseItemPayload`](/reference/2026-01-01/objects/createcompletedcourseitempayload)

## Example

```
mutation createCompletedCourseItem($input: createCompletedCourseItemInput!) {
  createCompletedCourseItem(input: $input) {
    completedCourseItem
    messages
    redirect_url
  }
}
```
