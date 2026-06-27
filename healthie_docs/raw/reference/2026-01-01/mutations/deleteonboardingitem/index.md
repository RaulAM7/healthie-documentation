---
title: deleteOnboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteonboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteonboardingitem/index.md
---

Destroy a OnboardingItem

## Arguments

[`input` ](#argument-input)· [`deleteOnboardingItemInput` ](/reference/2026-01-01/input-objects/deleteonboardingiteminput)· Parameters for deleteOnboardingItem

## Returns

[`deleteOnboardingItemPayload`](/reference/2026-01-01/objects/deleteonboardingitempayload)

## Example

```
mutation deleteOnboardingItem($input: deleteOnboardingItemInput) {
  deleteOnboardingItem(input: $input) {
    messages
    onboardingItem
  }
}
```
