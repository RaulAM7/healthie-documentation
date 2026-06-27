---
title: GoalInstance | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goalinstance/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goalinstance/index.md
---

a goal instance. gives a snapshot of a goal over a specific interval(start\_range and end\_range )

## Fields

[`end_range` ](#field-end-range)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date the interval starts for this goal instance

[`goal` ](#field-goal)· [`Goal` ](/reference/2026-01-01/objects/goal)· the relevant goal

[`is_completed_for_interval` ](#field-is-completed-for-interval)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the goal was completed in between the start and end range

[`start_range` ](#field-start-range)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· The date the interval starts for this goal instance

## Used By

[`GoalInstanceEdge.node`](/reference/2026-01-01/objects/goalinstanceedge)

[`GoalInstancePaginationConnection.nodes`](/reference/2026-01-01/objects/goalinstancepaginationconnection)

## Definition

```
"""
a goal instance. gives a snapshot of a goal over a specific interval(start_range and end_range )
"""
type GoalInstance {
  """
  The date the interval starts for this goal instance
  """
  end_range: ISO8601DateTime


  """
  the relevant goal
  """
  goal: Goal


  """
  If true, the goal was completed in between the start and end range
  """
  is_completed_for_interval: Boolean


  """
  The date the interval starts for this goal instance
  """
  start_range: ISO8601DateTime
}
```
