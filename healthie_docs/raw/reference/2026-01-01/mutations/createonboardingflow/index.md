---
title: createOnboardingFlow | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createonboardingflow/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createonboardingflow/index.md
---

create OnboardingFlow

## Arguments

[`input` ](#argument-input)· [`createOnboardingFlowInput` ](/reference/2026-01-01/input-objects/createonboardingflowinput)· Parameters for createOnboardingFlow

## Returns

[`createOnboardingFlowPayload`](/reference/2026-01-01/objects/createonboardingflowpayload)

## Example

```
mutation createOnboardingFlow($input: createOnboardingFlowInput) {
  createOnboardingFlow(input: $input) {
    messages
    onboardingFlow
  }
}
```
