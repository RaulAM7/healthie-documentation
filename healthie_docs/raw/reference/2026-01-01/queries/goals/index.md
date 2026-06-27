---
title: goals | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goals/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goals/index.md
---

All goals, either for a given user or for all of the providers clients

## Arguments

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`end_range` ](#argument-end-range)· [`String`](/reference/2026-01-01/scalars/string)

[`frequency_filter` ](#argument-frequency-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be daily, weekly, or one\_time

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`rel_goal_id` ](#argument-rel-goal-id)· [`String`](/reference/2026-01-01/scalars/string)

[`start_range` ](#argument-start-range)· [`String`](/reference/2026-01-01/scalars/string)

[`status_filter` ](#argument-status-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be complete or not\_complete

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`GoalOrderKeys`](/reference/2026-01-01/enums/goalorderkeys)

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`GoalPaginationConnection`](/reference/2026-01-01/objects/goalpaginationconnection)

## Example

```
query goals(
  $category: String
  $end_range: String
  $frequency_filter: String
  $keywords: String
  $rel_goal_id: String
  $start_range: String
  $status_filter: String
  $user_id: ID
  $sort_by: String
  $order_by: GoalOrderKeys
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  goals(
    category: $category
    end_range: $end_range
    frequency_filter: $frequency_filter
    keywords: $keywords
    rel_goal_id: $rel_goal_id
    start_range: $start_range
    status_filter: $status_filter
    user_id: $user_id
    sort_by: $sort_by
    order_by: $order_by
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
