---
title: goalInstances | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goalinstances/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goalinstances/index.md
---

A goal's instances

## Arguments

[`end_range` ](#argument-end-range)· [`String`](/reference/2026-01-01/scalars/string)

[`goal_id` ](#argument-goal-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`start_range` ](#argument-start-range)· [`String`](/reference/2026-01-01/scalars/string)

[`status_filter` ](#argument-status-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be complete or not\_complete

[`after` ](#argument-after)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come after the specified cursor.

[`before` ](#argument-before)· [`String` ](/reference/2026-01-01/scalars/string)· Returns the elements in the list that come before the specified cursor.

[`first` ](#argument-first)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the first \_n\_ elements from the list.

[`last` ](#argument-last)· [`Int` ](/reference/2026-01-01/scalars/int)· Returns the last \_n\_ elements from the list.

## Returns

[`GoalInstancePaginationConnection`](/reference/2026-01-01/objects/goalinstancepaginationconnection)

## Example

```
query goalInstances(
  $end_range: String
  $goal_id: ID
  $keywords: String
  $start_range: String
  $status_filter: String
  $after: String
  $before: String
  $first: Int
  $last: Int
) {
  goalInstances(
    end_range: $end_range
    goal_id: $goal_id
    keywords: $keywords
    start_range: $start_range
    status_filter: $status_filter
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
