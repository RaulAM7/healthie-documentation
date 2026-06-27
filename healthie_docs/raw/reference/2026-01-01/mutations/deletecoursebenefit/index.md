---
title: deleteCourseBenefit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecoursebenefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecoursebenefit/index.md
---

Destroy a Course Benefit

## Arguments

[`input` ](#argument-input)· [`deleteCourseBenefitInput` ](/reference/2026-01-01/input-objects/deletecoursebenefitinput)· Parameters for deleteCourseBenefit

## Returns

[`deleteCourseBenefitPayload`](/reference/2026-01-01/objects/deletecoursebenefitpayload)

## Example

```
mutation deleteCourseBenefit($input: deleteCourseBenefitInput) {
  deleteCourseBenefit(input: $input) {
    courseBenefit
    messages
  }
}
```
