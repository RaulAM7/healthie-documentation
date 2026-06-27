---
title: unassociatedCompletedOnboardingItems | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/unassociatedcompletedonboardingitems/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/unassociatedcompletedonboardingitems/index.md
---

Fetch paginated unassociated completed onboarding items collection

## Arguments

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· User to get unassociated onboarding items

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`CompletedOnboardingItemPaginationConnection`](/reference/2026-01-01/objects/completedonboardingitempaginationconnection)

## Example

```
query unassociatedCompletedOnboardingItems(
  $user_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  unassociatedCompletedOnboardingItems(
    user_id: $user_id
    after: $after
    before: $before
    first: $first
    last: $last
  ) {
    edges
    nodes
    page_info
    total_count
  }
}
```
