---
title: SubgoalInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/subgoalinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/subgoalinput/index.md
---

Payload for a sub-goal

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not this sub-goal should be deleted

[`created_user_id` ](#field-created-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user who created it

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the sub-goal

[`due_date` ](#field-due-date)· [`String` ](/reference/2026-01-01/scalars/string)· The date the sub-goal should end - format should be: yyyy-mm-dd

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the sub-goal. If no id is given, a sub-goal will be created

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The graphql\_name of the sub-goal

[`parent_id` ](#field-parent-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the parent goal

[`repeat` ](#field-repeat)· [`String` ](/reference/2026-01-01/scalars/string)· The frequency of this goal. Possible values are: 'Daily','Weekly', 'Once'

[`source_template_id` ](#field-source-template-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the sub-goal's template used to create this sub-goal

[`title_link` ](#field-title-link)· [`String` ](/reference/2026-01-01/scalars/string)· The sub-goal title hyperlink. Opens when the sub-goal graphql\_name is clicked on.

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the user who created this sub-goal. If no user\_id is given, the current user will be used

## Used By

[`createGoalInput.subgoals`](/reference/2026-01-01/input-objects/creategoalinput)

[`updateGoalInput.subgoals`](/reference/2026-01-01/input-objects/updategoalinput)

## Definition

```
"""
Payload for a sub-goal
"""
input SubgoalInput {
  """
  Whether or not this sub-goal should be deleted
  """
  _destroy: Boolean


  """
  The ID of the user who created it
  """
  created_user_id: String


  """
  The description of the sub-goal
  """
  description: String


  """
  The date the sub-goal should end - format should be: yyyy-mm-dd
  """
  due_date: String


  """
  The ID of the sub-goal. If no id is given, a sub-goal will be created
  """
  id: ID


  """
  The graphql_name of the sub-goal
  """
  name: String


  """
  The ID of the parent goal
  """
  parent_id: String


  """
  The frequency of this goal. Possible values are: 'Daily','Weekly', 'Once'
  """
  repeat: String


  """
  The ID of the sub-goal's template used to create this sub-goal
  """
  source_template_id: String


  """
  The sub-goal title hyperlink. Opens when the sub-goal graphql_name is clicked on.
  """
  title_link: String


  """
  The ID of the user who created this sub-goal. If no user_id is given, the current user will be used
  """
  user_id: String
}
```
