---
title: Reminder | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/reminder/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/reminder/index.md
---

A reminder object

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the reminder

[`interval_type` ](#field-interval-type)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Interval of a reminder ex. daily

[`interval_value` ](#field-interval-value)· [`String` ](/reference/2026-01-01/scalars/string)· Value of the reminder interval ex. monday

[`is_enabled` ](#field-is-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if reminder is active

## Used By

[`Goal.reminder`](/reference/2026-01-01/objects/goal)

[`Task.reminder`](/reference/2026-01-01/objects/task)

## Definition

```
"""
A reminder object
"""
type Reminder {
  """
  The unique identifier of the reminder
  """
  id: ID!


  """
  Interval of a reminder ex. daily
  """
  interval_type: String!


  """
  Value of the reminder interval ex. monday
  """
  interval_value: String


  """
  True if reminder is active
  """
  is_enabled: Boolean!
}
```
