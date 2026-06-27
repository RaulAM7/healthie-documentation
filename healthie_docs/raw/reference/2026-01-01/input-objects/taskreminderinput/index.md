---
title: TaskReminderInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/taskreminderinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/taskreminderinput/index.md
---

Payload for a task reminder

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· Id of the reminder. If no id is given, a reminder will be created

[`interval_type` ](#field-interval-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of interval. Options are daily, weekly, once

[`interval_value` ](#field-interval-value)· [`String` ](/reference/2026-01-01/scalars/string)· For a daily interval send nothing. For a weekly interval, send a comma separated day of week in the lower case (e.g wednesday, friday). To remind once, send the date (e.g 2020-11-28)

[`is_enabled` ](#field-is-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If not set to true, the reminder will not be sent

[`reminder_time` ](#field-reminder-time)· [`Int` ](/reference/2026-01-01/scalars/int)· Time for reminder

[`remove_reminder` ](#field-remove-reminder)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send in true to delete the reminder

## Used By

[`createTaskInput.reminder`](/reference/2026-01-01/input-objects/createtaskinput)

[`updateTaskInput.reminder`](/reference/2026-01-01/input-objects/updatetaskinput)

## Definition

```
"""
Payload for a task reminder
"""
input TaskReminderInput {
  """
  Id of the reminder. If no id is given, a reminder will be created
  """
  id: ID


  """
  The type of interval. Options are daily, weekly, once
  """
  interval_type: String


  """
  For a daily interval send nothing. For a weekly interval, send a comma separated day of week in the lower case (e.g wednesday, friday). To remind once, send the date (e.g 2020-11-28)
  """
  interval_value: String


  """
  If not set to true, the reminder will not be sent
  """
  is_enabled: Boolean


  """
  Time for reminder
  """
  reminder_time: Int


  """
  Send in true to delete the reminder
  """
  remove_reminder: Boolean
}
```
