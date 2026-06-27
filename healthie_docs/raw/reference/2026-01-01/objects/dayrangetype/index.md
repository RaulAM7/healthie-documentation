---
title: DayRangeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/dayrangetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/dayrangetype/index.md
---

Each day range is a time range and the days of the week that are in that time range

## Fields

[`days` ](#field-days)· [`[String]` ](/reference/2026-01-01/scalars/string)· The days of the week that are in this time range

[`time_range` ](#field-time-range)· [`String` ](/reference/2026-01-01/scalars/string)· The time range that is in this time range

## Used By

[`RecurringDaysData.day_ranges`](/reference/2026-01-01/objects/recurringdaysdata)

## Definition

```
"""
Each day range is a time range and the days of the week that are in that time range
"""
type DayRangeType {
  """
  The days of the week that are in this time range
  """
  days: [String]


  """
  The time range that is in this time range
  """
  time_range: String
}
```
