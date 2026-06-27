---
title: updateCourseMembership | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecoursemembership/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecoursemembership/index.md
---

update a Course Membership

## Arguments

[`input` ](#argument-input)· [`updateCourseMembershipInput` ](/reference/2026-01-01/input-objects/updatecoursemembershipinput)· Parameters for updateCourseMembership

## Returns

[`updateCourseMembershipPayload`](/reference/2026-01-01/objects/updatecoursemembershippayload)

## Example

```
mutation updateCourseMembership($input: updateCourseMembershipInput) {
  updateCourseMembership(input: $input) {
    courseMembership
    messages
  }
}
```
