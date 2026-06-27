---
title: ReminderInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/reminderinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/reminderinput/index.md
---

Payload for a reminder

## Fields

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the reminder. If no id is given, a reminder will be created

[`interval_type` ](#field-interval-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of the reminder interval. Options are daily, weekly, once

[`interval_value` ](#field-interval-value)· [`String` ](/reference/2026-01-01/scalars/string)· For daily interval -> don't send anything. For weekly interval, send in comma separated all lower-case day of week (e.g wednesday, friday). For once, send in the date (e.g 2020-11-28)

[`is_enabled` ](#field-is-enabled)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If not set to true, the reminder will not be sent

[`remove_reminder` ](#field-remove-reminder)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Send in true to delete the reminder

## Used By

[`createGoalInput.reminder`](/reference/2026-01-01/input-objects/creategoalinput)

[`updateGoalInput.reminder`](/reference/2026-01-01/input-objects/updategoalinput)

## Definition

```
"""
Payload for a reminder
"""
input ReminderInput {
  """
  The ID of the reminder. If no id is given, a reminder will be created
  """
  id: ID


  """
  The type of the reminder interval. Options are daily, weekly, once
  """
  interval_type: String


  """
  For daily interval -> don't send anything. For weekly interval, send in comma separated all lower-case day of week (e.g wednesday, friday). For once, send in the date (e.g 2020-11-28)
  """
  interval_value: String


  """
  If not set to true, the reminder will not be sent
  """
  is_enabled: Boolean


  """
  Send in true to delete the reminder
  """
  remove_reminder: Boolean
}
```
