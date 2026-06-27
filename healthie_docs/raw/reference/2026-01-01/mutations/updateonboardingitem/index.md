---
title: updateOnboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateonboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateonboardingitem/index.md
---

Update a OnboardingItem and return OnboardingItem

## Arguments

[`input` ](#argument-input)· [`updateOnboardingItemInput` ](/reference/2026-01-01/input-objects/updateonboardingiteminput)· Parameters for updateOnboardingItem

## Returns

[`updateOnboardingItemPayload`](/reference/2026-01-01/objects/updateonboardingitempayload)

## Example

```
mutation updateOnboardingItem($input: updateOnboardingItemInput) {
  updateOnboardingItem(input: $input) {
    messages
    onboardingItem
  }
}
```
