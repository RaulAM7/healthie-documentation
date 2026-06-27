---
title: createCourseBenefit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcoursebenefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcoursebenefit/index.md
---

create CourseBenefit

## Arguments

[`input` ](#argument-input)· [`createCourseBenefitInput` ](/reference/2026-01-01/input-objects/createcoursebenefitinput)· Parameters for createCourseBenefit

## Returns

[`createCourseBenefitPayload`](/reference/2026-01-01/objects/createcoursebenefitpayload)

## Example

```
mutation createCourseBenefit($input: createCourseBenefitInput) {
  createCourseBenefit(input: $input) {
    courseBenefit
    messages
  }
}
```
