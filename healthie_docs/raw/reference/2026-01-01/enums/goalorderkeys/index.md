---
title: GoalOrderKeys | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/enums/goalorderkeys/index
  md: https://docs.gethealthie.com/reference/2026-01-01/enums/goalorderkeys/index.md
---

Goal sorting enum

## Used By

[`Query.goals`](/reference/2026-01-01/queries/goals)

[`Query.goalsData`](/reference/2026-01-01/queries/goalsdata)

## Definition

```
"""
Goal sorting enum
"""
enum GoalOrderKeys {
  START_DATE_ASC
  START_DATE_DESC
  FREQUENCY_ASC
  FREQUENCY_DESC
  NAME_ASC
  NAME_DESC
  CREATED_BY_ASC
  CREATED_BY_DESC
  STATUS_ASC
  STATUS_DESC
  DUE_DATE_ASC
  DUE_DATE_DESC


  """
  Order by due date and start date descending
  """
  DUE_DATE_START_DATE_DESC
}
```
