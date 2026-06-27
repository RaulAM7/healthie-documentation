---
title: deleteOnboardingFlow | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteonboardingflow/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteonboardingflow/index.md
---

Destroy a OnboardingFlow

## Arguments

[`input` ](#argument-input)· [`deleteOnboardingFlowInput` ](/reference/2026-01-01/input-objects/deleteonboardingflowinput)· Parameters for deleteOnboardingFlow

## Returns

[`deleteOnboardingFlowPayload`](/reference/2026-01-01/objects/deleteonboardingflowpayload)

## Example

```
mutation deleteOnboardingFlow($input: deleteOnboardingFlowInput) {
  deleteOnboardingFlow(input: $input) {
    messages
    onboardingFlow
  }
}
```
