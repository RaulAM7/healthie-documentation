---
title: GoalStreakInfo | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goalstreakinfo/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goalstreakinfo/index.md
---

Related info of a specific goal's streak

## Fields

[`count` ](#field-count)· [`Int` ](/reference/2026-01-01/scalars/int)· The length of intervals (ie: days, weeks, etc) this streak lasted

[`end_date` ](#field-end-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The day this streak ended

[`start_date` ](#field-start-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The day this streak began

## Used By

[`Goal.streak_info`](/reference/2026-01-01/objects/goal)

## Definition

```
"""
Related info of a specific goal's streak
"""
type GoalStreakInfo {
  """
  The length of intervals (ie: days, weeks, etc) this streak lasted
  """
  count: Int


  """
  The day this streak ended
  """
  end_date: ISO8601DateTime


  """
  The day this streak began
  """
  start_date: ISO8601DateTime
}
```
