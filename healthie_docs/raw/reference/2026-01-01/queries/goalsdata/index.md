---
title: goalsData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goalsdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goalsdata/index.md
---

All goals data

## Arguments

[`after` ](#argument-after)· [`Cursor` ](/reference/2026-01-01/scalars/cursor)· Cursor to fetch results after

[`category` ](#argument-category)· [`String` ](/reference/2026-01-01/scalars/string)· Search over goals' repeat property

[`end_range` ](#argument-end-range)· [`String`](/reference/2026-01-01/scalars/string)

[`frequency_filter` ](#argument-frequency-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be daily, weekly, or one\_time

[`keywords` ](#argument-keywords)· [`String` ](/reference/2026-01-01/scalars/string)· Search over goals' names and descriptions

[`offset` ](#argument-offset)· [`Int`](/reference/2026-01-01/scalars/int)

[`per_page` ](#argument-per-page)· [`Int`](/reference/2026-01-01/scalars/int)

[`rel_goal_id` ](#argument-rel-goal-id)· [`String` ](/reference/2026-01-01/scalars/string)· the goal ID

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`order_by` ](#argument-order-by)· [`GoalOrderKeys`](/reference/2026-01-01/enums/goalorderkeys)

[`start_range` ](#argument-start-range)· [`String`](/reference/2026-01-01/scalars/string)

[`status_filter` ](#argument-status-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be complete or not\_complete

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`GoalDataType`](/reference/2026-01-01/objects/goaldatatype)

## Example

```
query goalsData(
  $after: Cursor
  $category: String
  $end_range: String
  $frequency_filter: String
  $keywords: String
  $offset: Int
  $per_page: Int
  $rel_goal_id: String
  $sort_by: String
  $order_by: GoalOrderKeys
  $start_range: String
  $status_filter: String
  $user_id: ID
) {
  goalsData(
    after: $after
    category: $category
    end_range: $end_range
    frequency_filter: $frequency_filter
    keywords: $keywords
    offset: $offset
    per_page: $per_page
    rel_goal_id: $rel_goal_id
    sort_by: $sort_by
    order_by: $order_by
    start_range: $start_range
    status_filter: $status_filter
    user_id: $user_id
  ) {
    all_goals_frequency_count
    all_goals_status_count
    all_time_goals_count
    completed_goals_count
    daily_goals_count
    goals
    goals_count
    goals_overall_completion_rate_info
    goals_streak_count
    not_completed_goals_count
    one_time_goals_count
    weekly_goals_count
  }
}
```
