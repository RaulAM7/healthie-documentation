---
title: GoalDataType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goaldatatype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goaldatatype/index.md
---

Goal data

## Fields

[`all_goals_frequency_count` ](#field-all-goals-frequency-count)· [`Int` ](/reference/2026-01-01/scalars/int)· All goals frequency count

[`all_goals_status_count` ](#field-all-goals-status-count)· [`Int` ](/reference/2026-01-01/scalars/int)· All goals status count

[`all_time_goals_count` ](#field-all-time-goals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· All time goals count

[`completed_goals_count` ](#field-completed-goals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Completed goals count

[`daily_goals_count` ](#field-daily-goals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Daily goals count

[`goals` ](#field-goals)· [`[Goal!]` ](/reference/2026-01-01/objects/goal)· Goal list

[`goals_count` ](#field-goals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Goals count

[`goals_overall_completion_rate_info` ](#field-goals-overall-completion-rate-info)· [`GoalOverallCompletionRateInfo` ](/reference/2026-01-01/objects/goaloverallcompletionrateinfo)· Goals overall completion rate info

[`goals_streak_count` ](#field-goals-streak-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Goals streak count

[`not_completed_goals_count` ](#field-not-completed-goals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Not completed goals count

[`one_time_goals_count` ](#field-one-time-goals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· One time goals count

[`weekly_goals_count` ](#field-weekly-goals-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Weekly goals count

## Used By

[`Query.goalsData`](/reference/2026-01-01/queries/goalsdata)

## Definition

```
"""
Goal data
"""
type GoalDataType {
  """
  All goals frequency count
  """
  all_goals_frequency_count: Int


  """
  All goals status count
  """
  all_goals_status_count: Int


  """
  All time goals count
  """
  all_time_goals_count: Int


  """
  Completed goals count
  """
  completed_goals_count: Int


  """
  Daily goals count
  """
  daily_goals_count: Int


  """
  Goal list
  """
  goals: [Goal!]


  """
  Goals count
  """
  goals_count: Int


  """
  Goals overall completion rate info
  """
  goals_overall_completion_rate_info: GoalOverallCompletionRateInfo


  """
  Goals streak count
  """
  goals_streak_count: Int


  """
  Not completed goals count
  """
  not_completed_goals_count: Int


  """
  One time goals count
  """
  one_time_goals_count: Int


  """
  Weekly goals count
  """
  weekly_goals_count: Int
}
```
