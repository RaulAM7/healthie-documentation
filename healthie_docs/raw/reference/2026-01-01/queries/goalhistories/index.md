---
title: goalHistories | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goalhistories/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goalhistories/index.md
---

All completed goals for a given set of users

## Arguments

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`include_subgoals` ](#argument-include-subgoals)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`unique` ](#argument-unique)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`GoalHistoryPaginationConnection`](/reference/2026-01-01/objects/goalhistorypaginationconnection)

## Example

```
query goalHistories(
  $category: String
  $include_subgoals: Boolean
  $unique: Boolean
  $user_id: ID
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  goalHistories(
    category: $category
    include_subgoals: $include_subgoals
    unique: $unique
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
