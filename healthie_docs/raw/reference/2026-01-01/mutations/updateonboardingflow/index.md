---
title: updateOnboardingFlow | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateonboardingflow/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateonboardingflow/index.md
---

Update a OnboardingFlow and return OnboardingFlow

## Arguments

[`input` ](#argument-input)· [`updateOnboardingFlowInput` ](/reference/2026-01-01/input-objects/updateonboardingflowinput)· Parameters for updateOnboardingFlow

## Returns

[`updateOnboardingFlowPayload`](/reference/2026-01-01/objects/updateonboardingflowpayload)

## Example

```
mutation updateOnboardingFlow($input: updateOnboardingFlowInput) {
  updateOnboardingFlow(input: $input) {
    messages
    onboardingFlow
  }
}
```
