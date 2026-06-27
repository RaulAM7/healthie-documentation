---
title: DayRangeInputObjectType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/dayrangeinputobjecttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/dayrangeinputobjecttype/index.md
---

The day range input

## Fields

[`days` ](#field-days)· [`[String]` ](/reference/2026-01-01/scalars/string)· The days range

[`time_range` ](#field-time-range)· [`String` ](/reference/2026-01-01/scalars/string)· The time range for every day

## Used By

[`RecurringDaysInputObjectType.day_ranges`](/reference/2026-01-01/input-objects/recurringdaysinputobjecttype)

## Definition

```
"""
The day range input
"""
input DayRangeInputObjectType {
  """
  The days range
  """
  days: [String]


  """
  The time range for every day
  """
  time_range: String
}
```
