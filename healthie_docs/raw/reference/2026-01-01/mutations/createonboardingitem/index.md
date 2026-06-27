---
title: createOnboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createonboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createonboardingitem/index.md
---

create OnboardingItem

## Arguments

[`input` ](#argument-input)· [`createOnboardingItemInput` ](/reference/2026-01-01/input-objects/createonboardingiteminput)· Parameters for createOnboardingItem

## Returns

[`createOnboardingItemPayload`](/reference/2026-01-01/objects/createonboardingitempayload)

## Example

```
mutation createOnboardingItem($input: createOnboardingItemInput) {
  createOnboardingItem(input: $input) {
    messages
    onboardingItem
  }
}
```
