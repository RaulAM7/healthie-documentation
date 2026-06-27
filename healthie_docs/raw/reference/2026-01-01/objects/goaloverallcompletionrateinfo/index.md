---
title: GoalOverallCompletionRateInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goaloverallcompletionrateinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goaloverallcompletionrateinfo/index.md
---

Related info for a collection of goals overall completion rate

## Fields

[`actual_times_completed` ](#field-actual-times-completed)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of times the goals were completed

[`percent` ](#field-percent)· [`Int` ](/reference/2026-01-01/scalars/int)· The actual percentage of the completion rate

[`possible_times_completed` ](#field-possible-times-completed)· [`Int` ](/reference/2026-01-01/scalars/int)· The total number of times the goals could have been completed

## Used By

[`GoalDataType.goals_overall_completion_rate_info`](/reference/2026-01-01/objects/goaldatatype)

[`Query.goalsOverallCompletionRateInfo`](/reference/2026-01-01/queries/goalsoverallcompletionrateinfo)

## Definition

```
"""
Related info for a collection of goals overall completion rate
"""
type GoalOverallCompletionRateInfo {
  """
  The number of times the goals were completed
  """
  actual_times_completed: Int


  """
  The actual percentage of the completion rate
  """
  percent: Int


  """
  The total number of times the goals could have been completed
  """
  possible_times_completed: Int
}
```
