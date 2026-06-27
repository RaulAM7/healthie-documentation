---
title: GoalHistory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goalhistory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goalhistory/index.md
---

a goal history

## Fields

[`action` ](#field-action)· [`GoalHistoryActionTypeEnum` ](/reference/2026-01-01/enums/goalhistoryactiontypeenum)· The action type that was performed on a specific goal that created this history record

[`completed_on` ](#field-completed-on)· [`ISO8601Date!` ](/reference/2026-01-01/scalars/iso8601date)· required · The date the goal is marked completed

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The completion timestamp of the goal

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the goal

[`goal` ](#field-goal)· [`Goal` ](/reference/2026-01-01/objects/goal)· goal that was completed

[`goal_id` ](#field-goal-id)· [`ID` ](/reference/2026-01-01/scalars/id)· goal id of goal history

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the history

[`is_subgoal` ](#field-is-subgoal)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the goal is a subgoal

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the goal

[`repeat` ](#field-repeat)· [`String` ](/reference/2026-01-01/scalars/string)· The repeat frequency of the goal

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· client of this goal

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· user id of goal history

## Used By

[`Goal.goal_histories`](/reference/2026-01-01/objects/goal)

[`GoalHistoryEdge.node`](/reference/2026-01-01/objects/goalhistoryedge)

[`GoalHistoryPaginationConnection.nodes`](/reference/2026-01-01/objects/goalhistorypaginationconnection)

[`createGoalHistoryPayload.goalHistory`](/reference/2026-01-01/objects/creategoalhistorypayload)

[`deleteGoalHistoryPayload.goal_history`](/reference/2026-01-01/objects/deletegoalhistorypayload)

[`Query.goalHistory`](/reference/2026-01-01/queries/goalhistory)

## Definition

```
"""
a goal history
"""
type GoalHistory {
  """
  The action type that was performed on a specific goal that created this history record
  """
  action: GoalHistoryActionTypeEnum


  """
  The date the goal is marked completed
  """
  completed_on: ISO8601Date!


  """
  The completion timestamp of the goal
  """
  created_at: ISO8601DateTime!


  """
  The description of the goal
  """
  description: String


  """
  goal that was completed
  """
  goal: Goal


  """
  goal id of goal history
  """
  goal_id: ID


  """
  The unique identifier of the history
  """
  id: ID!


  """
  If true, the goal is a subgoal
  """
  is_subgoal: Boolean


  """
  The name of the goal
  """
  name: String


  """
  The repeat frequency of the goal
  """
  repeat: String


  """
  client of this goal
  """
  user: User


  """
  user id of goal history
  """
  user_id: ID
}
```
