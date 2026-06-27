---
title: goal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/goal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/goal/index.md
---

fetch a goal by id

## Arguments

[`client_id` ](#argument-client-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`date` ](#argument-date)· [`String`](/reference/2026-01-01/scalars/string)

[`get_client_goal` ](#argument-get-client-goal)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`id` ](#argument-id)· [`ID`](/reference/2026-01-01/scalars/id)

[`last_client_goal` ](#argument-last-client-goal)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Deprecated, at some point this argument stopped being used. Keeping it around in order to make sure nothing breaks backwards

[`patient_goal_module` ](#argument-patient-goal-module)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

[`program_goal` ](#argument-program-goal)· [`Boolean`](/reference/2026-01-01/scalars/boolean)

## Returns

[`Goal`](/reference/2026-01-01/objects/goal)

## Example

```
query goal(
  $client_id: ID
  $date: String
  $get_client_goal: Boolean
  $id: ID
  $last_client_goal: Boolean
  $patient_goal_module: Boolean
  $program_goal: Boolean
) {
  goal(
    client_id: $client_id
    date: $date
    get_client_goal: $get_client_goal
    id: $id
    last_client_goal: $last_client_goal
    patient_goal_module: $patient_goal_module
    program_goal: $program_goal
  ) {
    completion_percentage_for_range
    created_at
    created_user
    created_user_id
    description
    due_date
    goal_histories
    id
    is_completed_for_date
    is_used_as_template
    name
    parent_id
    parent_subgoal_completion_rate
    reminder
    repeat
    source_template_id
    start_on
    streak_info
    subgoals
    subgoals_count
    title_link
    user
    user_id
  }
}
```
