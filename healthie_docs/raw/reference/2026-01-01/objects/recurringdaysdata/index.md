---
title: RecurringDaysData | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringdaysdata/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recurringdaysdata/index.md
---

Each data point has a time range and the days that are in that time range

## Fields

[`day_ranges` ](#field-day-ranges)· [`[DayRangeType!]` ](/reference/2026-01-01/objects/dayrangetype)· The days that are in the time range

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the recurring days data

## Used By

[`ChatSetting.recurring_days_data`](/reference/2026-01-01/objects/chatsetting)

## Definition

```
"""
Each data point has a time range and the days that are in that time range
"""
type RecurringDaysData {
  """
  The days that are in the time range
  """
  day_ranges: [DayRangeType!]


  """
  The unique identifier of the recurring days data
  """
  id: ID!
}
```
