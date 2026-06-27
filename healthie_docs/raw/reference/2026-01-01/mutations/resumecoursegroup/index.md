---
title: resumeCourseGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/resumecoursegroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/resumecoursegroup/index.md
---

Resume a paused course group, bulk-resuming all paused member enrollments

## Arguments

[`input` ](#argument-input)· [`ResumeCourseGroupInput!` ](/reference/2026-01-01/input-objects/resumecoursegroupinput)· required · Parameters for ResumeCourseGroup

## Returns

[`ResumeCourseGroupPayload`](/reference/2026-01-01/objects/resumecoursegrouppayload)

## Example

```
mutation resumeCourseGroup($input: ResumeCourseGroupInput!) {
  resumeCourseGroup(input: $input) {
    courseGroup
    messages
  }
}
```
