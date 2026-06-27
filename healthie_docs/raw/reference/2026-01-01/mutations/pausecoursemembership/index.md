---
title: pauseCourseMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/pausecoursemembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/pausecoursemembership/index.md
---

Pause a client's program enrollment

## Arguments

[`input` ](#argument-input)· [`PauseCourseMembershipInput!` ](/reference/2026-01-01/input-objects/pausecoursemembershipinput)· required · Parameters for PauseCourseMembership

## Returns

[`PauseCourseMembershipPayload`](/reference/2026-01-01/objects/pausecoursemembershippayload)

## Example

```
mutation pauseCourseMembership($input: PauseCourseMembershipInput!) {
  pauseCourseMembership(input: $input) {
    courseMembership
    messages
  }
}
```
