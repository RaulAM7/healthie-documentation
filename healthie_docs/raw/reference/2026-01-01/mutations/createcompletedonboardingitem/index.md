---
title: createCompletedOnboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcompletedonboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcompletedonboardingitem/index.md
---

create CompletedOnboardingItem

## Arguments

[`input` ](#argument-input)· [`createCompletedOnboardingItemInput` ](/reference/2026-01-01/input-objects/createcompletedonboardingiteminput)· Parameters for createCompletedOnboardingItem

## Returns

[`createCompletedOnboardingItemPayload`](/reference/2026-01-01/objects/createcompletedonboardingitempayload)

## Example

```
mutation createCompletedOnboardingItem(
  $input: createCompletedOnboardingItemInput
) {
  createCompletedOnboardingItem(input: $input) {
    completed_onboarding_item
    messages
  }
}
```
