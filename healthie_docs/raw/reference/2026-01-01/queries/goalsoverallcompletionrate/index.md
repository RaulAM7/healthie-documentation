---
title: goalsOverallCompletionRate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goalsoverallcompletionrate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goalsoverallcompletionrate/index.md
---

deprecated Use goalsOverallCompletionRateInfo instead

Overall completion percentage of goals

## Arguments

[`category` ](#argument-category)· [`String`](/reference/2026-01-01/scalars/string)

[`end_range` ](#argument-end-range)· [`String`](/reference/2026-01-01/scalars/string)

[`frequency_filter` ](#argument-frequency-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be daily, weekly, or one\_time

[`keywords` ](#argument-keywords)· [`String`](/reference/2026-01-01/scalars/string)

[`offset` ](#argument-offset)· [`Int`](/reference/2026-01-01/scalars/int)

[`rel_goal_id` ](#argument-rel-goal-id)· [`String`](/reference/2026-01-01/scalars/string)

[`sort_by` ](#argument-sort-by)· [`String`](/reference/2026-01-01/scalars/string)

[`start_range` ](#argument-start-range)· [`String`](/reference/2026-01-01/scalars/string)

[`status_filter` ](#argument-status-filter)· [`String` ](/reference/2026-01-01/scalars/string)· Can be complete or not\_complete

[`user_id` ](#argument-user-id)· [`ID`](/reference/2026-01-01/scalars/id)

## Returns

[`Int`](/reference/2026-01-01/scalars/int)

## Example

```
query goalsOverallCompletionRate(
  $category: String
  $end_range: String
  $frequency_filter: String
  $keywords: String
  $offset: Int
  $rel_goal_id: String
  $sort_by: String
  $start_range: String
  $status_filter: String
  $user_id: ID
) {
  goalsOverallCompletionRate(
    category: $category
    end_range: $end_range
    frequency_filter: $frequency_filter
    keywords: $keywords
    offset: $offset
    rel_goal_id: $rel_goal_id
    sort_by: $sort_by
    start_range: $start_range
    status_filter: $status_filter
    user_id: $user_id
  )
}
```
