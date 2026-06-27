---
title: scheduledUserPackageSelections | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/scheduleduserpackageselections/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/scheduleduserpackageselections/index.md
---

Fetch paginated scheduled user package selections collection

## Arguments

[`offering_id` ](#argument-offering-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the offering to filter the list

[`user_id` ](#argument-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· ID of the user to load the list of given packages

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`ScheduledUserPackageSelectionPaginationConnection`](/reference/2026-01-01/objects/scheduleduserpackageselectionpaginationconnection)

## Example

```
query scheduledUserPackageSelections(
  $offering_id: ID
  $user_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  scheduledUserPackageSelections(
    offering_id: $offering_id
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
