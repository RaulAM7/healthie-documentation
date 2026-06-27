---
title: healthAssessmentServiceSignup | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/healthassessmentservicesignup/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/healthassessmentservicesignup/index.md
---

deprecated Deprecated, do not use

Sign up Healthie User in the Health Assessment Service

## Arguments

[`input` ](#argument-input)· [`HealthAssessmentServiceSignupInput` ](/reference/2026-01-01/input-objects/healthassessmentservicesignupinput)· Parameters for HealthAssessmentServiceSignup

## Returns

[`HealthAssessmentServiceSignupPayload`](/reference/2026-01-01/objects/healthassessmentservicesignuppayload)

## Example

```
mutation healthAssessmentServiceSignup(
  $input: HealthAssessmentServiceSignupInput
) {
  healthAssessmentServiceSignup(input: $input) {
    deeplink_url
    messages
  }
}
```
