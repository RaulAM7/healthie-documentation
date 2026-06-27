---
title: deleteCourseMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecoursemembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecoursemembership/index.md
---

Destroy a Course Membership

## Arguments

[`input` ](#argument-input)· [`deleteCourseMembershipInput` ](/reference/2026-01-01/input-objects/deletecoursemembershipinput)· Parameters for deleteCourseMembership

## Returns

[`deleteCourseMembershipPayload`](/reference/2026-01-01/objects/deletecoursemembershippayload)

## Example

```
mutation deleteCourseMembership($input: deleteCourseMembershipInput) {
  deleteCourseMembership(input: $input) {
    courseMembership
    messages
  }
}
```
