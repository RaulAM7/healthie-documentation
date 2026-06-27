---
title: RecurringDaysInputObjectType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/recurringdaysinputobjecttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/recurringdaysinputobjecttype/index.md
---

The recurring days input

## Fields

[`day_ranges` ](#field-day-ranges)· [`[DayRangeInputObjectType]` ](/reference/2026-01-01/input-objects/dayrangeinputobjecttype)· The list of day ranges

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the recurring day

## Used By

[`createChatSettingInput.recurring_days_data`](/reference/2026-01-01/input-objects/createchatsettinginput)

[`updateChatSettingInput.recurring_days_data`](/reference/2026-01-01/input-objects/updatechatsettinginput)

## Definition

```
"""
The recurring days input
"""
input RecurringDaysInputObjectType {
  """
  The list of day ranges
  """
  day_ranges: [DayRangeInputObjectType]


  """
  The id of the recurring day
  """
  id: ID
}
```
