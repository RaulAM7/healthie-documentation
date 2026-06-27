---
title: resumeCourseMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/resumecoursemembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/resumecoursemembership/index.md
---

Resume a paused program enrollment

## Arguments

[`input` ](#argument-input)· [`ResumeCourseMembershipInput!` ](/reference/2026-01-01/input-objects/resumecoursemembershipinput)· required · Parameters for ResumeCourseMembership

## Returns

[`ResumeCourseMembershipPayload`](/reference/2026-01-01/objects/resumecoursemembershippayload)

## Example

```
mutation resumeCourseMembership($input: ResumeCourseMembershipInput!) {
  resumeCourseMembership(input: $input) {
    courseMembership
    messages
  }
}
```
