---
title: pauseCourseGroup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/pausecoursegroup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/pausecoursegroup/index.md
---

Pause a course group, bulk-pausing all active member enrollments

## Arguments

[`input` ](#argument-input)· [`PauseCourseGroupInput!` ](/reference/2026-01-01/input-objects/pausecoursegroupinput)· required · Parameters for PauseCourseGroup

## Returns

[`PauseCourseGroupPayload`](/reference/2026-01-01/objects/pausecoursegrouppayload)

## Example

```
mutation pauseCourseGroup($input: PauseCourseGroupInput!) {
  pauseCourseGroup(input: $input) {
    courseGroup
    messages
  }
}
```
