---
title: completedOnboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/completedonboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/completedonboardingitem/index.md
---

Get the completed onboarding item by ID

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The ID of the completed onboarding item

## Returns

[`CompletedOnboardingItem`](/reference/2026-01-01/objects/completedonboardingitem)

## Example

```
query completedOnboardingItem($id: ID!) {
  completedOnboardingItem(id: $id) {
    attached_object_edit_url
    date_to_show
    id
    item_id
    item_type
    onboarding_item
    onboarding_item_id
    skipped
    user
    user_id
    view_url
  }
}
```
