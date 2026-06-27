---
title: onboardingFlow | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/onboardingflow/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/onboardingflow/index.md
---

Fetch an onboarding flow by id or uuid

## Arguments

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`uuid` ](#argument-uuid)· [`String` ](/reference/2026-01-01/scalars/string)· Fetch onboarding flow by unique identifier. Considered public

## Returns

[`OnboardingFlow`](/reference/2026-01-01/objects/onboardingflow)

## Example

```
query onboardingFlow($id: ID, $user_id: ID, $uuid: String) {
  onboardingFlow(id: $id, user_id: $user_id, uuid: $uuid) {
    created_at
    has_forms_after_welcome
    id
    is_multiple_providers
    name
    onboarding_items
    onboarding_items_count
    user
    user_groups
    user_groups_count
    user_groups_name_string
  }
}
```
