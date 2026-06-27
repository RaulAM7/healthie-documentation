---
title: onboardingItem | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/onboardingitem/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/onboardingitem/index.md
---

fetch an onboarding item by id (considered public)

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Patient ID who owns the form

[`track_opened_event` ](#argument-track-opened-event)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If TRUE, create form history 'opened' event

## Returns

[`OnboardingItem`](/reference/2026-01-01/objects/onboardingitem)

## Example

```
query onboardingItem($id: ID!, $user_id: ID, $track_opened_event: Boolean) {
  onboardingItem(
    id: $id
    user_id: $user_id
    track_opened_event: $track_opened_event
  ) {
    attached_object_edit_url
    billing_disclaimer
    completed_form_id
    completed_onboarding_item
    date_to_show
    display_name
    has_matrix_field
    id
    incomplete_form_id
    is_last_item
    is_skippable
    item_id
    item_type
    onboarding_flow
    onboarding_flow_id
    photo_id_disclaimer
    policy_disclaimer
    user
    view_url
    welcome_text
  }
}
```
