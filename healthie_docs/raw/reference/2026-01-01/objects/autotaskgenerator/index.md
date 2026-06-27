---
title: AutoTaskGenerator | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/autotaskgenerator/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/autotaskgenerator/index.md
---

The auto task generators belonging to a specific user

## Fields

[`category` ](#field-category)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Category of task

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time that the task was created

[`days_due_from_created_at` ](#field-days-due-from-created-at)· [`Int` ](/reference/2026-01-01/scalars/int)· The number of days the task is due from the date it was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the generator

[`is_enabled` ](#field-is-enabled)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · True if task is active

[`number_description` ](#field-number-description)· [`String` ](/reference/2026-01-01/scalars/string)· Description of the number to check

[`number_to_check` ](#field-number-to-check)· [`Float!` ](/reference/2026-01-01/scalars/float)· required · The number to check

[`task_description` ](#field-task-description)· [`String!` ](/reference/2026-01-01/scalars/string)· required · Description of the task

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The last date and time that the task was updated

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the user who creates the task

[`user_id_for_task` ](#field-user-id-for-task)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the user

## Used By

[`AutoTaskGeneratorEdge.node`](/reference/2026-01-01/objects/autotaskgeneratoredge)

[`AutoTaskGeneratorPaginationConnection.nodes`](/reference/2026-01-01/objects/autotaskgeneratorpaginationconnection)

[`createAutoTaskGeneratorPayload.auto_task_generator`](/reference/2026-01-01/objects/createautotaskgeneratorpayload)

[`deleteAutoTaskGeneratorPayload.auto_task_generator`](/reference/2026-01-01/objects/deleteautotaskgeneratorpayload)

[`updateAutoTaskGeneratorPayload.auto_task_generator`](/reference/2026-01-01/objects/updateautotaskgeneratorpayload)

## Definition

```
"""
The auto task generators belonging to a specific user
"""
type AutoTaskGenerator {
  """
  Category of task
  """
  category: String!


  """
  The date and time that the task was created
  """
  created_at: ISO8601DateTime!


  """
  The number of days the task is due from the date it was created
  """
  days_due_from_created_at: Int


  """
  The unique identifier of the generator
  """
  id: ID!


  """
  True if task is active
  """
  is_enabled: Boolean!


  """
  Description of the number to check
  """
  number_description: String


  """
  The number to check
  """
  number_to_check: Float!


  """
  Description of the task
  """
  task_description: String!


  """
  The last date and time that the task was updated
  """
  updated_at: ISO8601DateTime!


  """
  The id of the user who creates the task
  """
  user_id: String


  """
  The id of the user
  """
  user_id_for_task: String
}
```
