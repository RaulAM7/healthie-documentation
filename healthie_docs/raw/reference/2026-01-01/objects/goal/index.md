---
title: Goal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goal/index.md
---

a goal

## Fields

[`completion_percentage_for_range` ](#field-completion-percentage-for-range)· [`Int` ](/reference/2026-01-01/scalars/int)· Completion Percentage of a goal for a given date range. start\_range/end\_range should be of the form: 'yyyy-mm-dd'

[`completion_rate` ](#field-completion-rate)· [`String` ](/reference/2026-01-01/scalars/string)· The rate at which this goal is completed

deprecated

should use completion\_percentage\_for\_range

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The creation timestamp of the goal

[`created_user` ](#field-created-user)· [`User` ](/reference/2026-01-01/objects/user)· User who created this goal

[`created_user_id` ](#field-created-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· created user of goal

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· description of goal

[`due_date` ](#field-due-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· due date of goal

[`goal_histories` ](#field-goal-histories)· [`[GoalHistory!]!` ](/reference/2026-01-01/objects/goalhistory)· required · All goal histories associated with this goal histories.

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the goal

[`is_completed_for_date` ](#field-is-completed-for-date)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the goal is complete for the given day. date should be of the form: 'yyyy-mm-dd'

[`is_current` ](#field-is-current)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· if true, the goal is currently active

deprecated

should use is\_completed\_for\_date field to determine if a goal is completed for a given day

[`is_used_as_template` ](#field-is-used-as-template)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· if true, a template has been created based off this goal

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of goal

[`parent_id` ](#field-parent-id)· [`ID` ](/reference/2026-01-01/scalars/id)· parent id

[`parent_subgoal_completion_rate` ](#field-parent-subgoal-completion-rate)· [`String` ](/reference/2026-01-01/scalars/string)· The rate at which the parent goal has subgoals completed

[`reminder` ](#field-reminder)· [`Reminder` ](/reference/2026-01-01/objects/reminder)· Reminder object for a given goal

[`repeat` ](#field-repeat)· [`String` ](/reference/2026-01-01/scalars/string)· frequency of goal

[`source_template_id` ](#field-source-template-id)· [`String` ](/reference/2026-01-01/scalars/string)· The id of the template used to make this goal

[`start_on` ](#field-start-on)· [`ISO8601Date!` ](/reference/2026-01-01/scalars/iso8601date)· required · start date of goal

[`streak_info` ](#field-streak-info)· [`[GoalStreakInfo!]` ](/reference/2026-01-01/objects/goalstreakinfo)· Streak info for goal

[`subgoal_completion_rate` ](#field-subgoal-completion-rate)· [`String` ](/reference/2026-01-01/scalars/string)· The rate at which a subgoal is completed

deprecated

should use completion\_percentage\_for\_range

[`subgoals` ](#field-subgoals)· [`[Goal!]` ](/reference/2026-01-01/objects/goal)· Subgoals for a given goal

[`subgoals_count` ](#field-subgoals-count)· [`String` ](/reference/2026-01-01/scalars/string)· count of subgoals

[`title_link` ](#field-title-link)· [`String` ](/reference/2026-01-01/scalars/string)· Title hyperlink. Opens when the title is clicked on.

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of this goal

[`user_id` ](#field-user-id)· [`ID` ](/reference/2026-01-01/scalars/id)· user id of goal

## Used By

[`CarePlan.goals`](/reference/2026-01-01/objects/careplan)

[`Goal.subgoals`](/reference/2026-01-01/objects/goal)

[`GoalDataType.goals`](/reference/2026-01-01/objects/goaldatatype)

[`GoalEdge.node`](/reference/2026-01-01/objects/goaledge)

[`GoalHistory.goal`](/reference/2026-01-01/objects/goalhistory)

[`GoalInstance.goal`](/reference/2026-01-01/objects/goalinstance)

[`GoalPaginationConnection.nodes`](/reference/2026-01-01/objects/goalpaginationconnection)

[`createGoalPayload.goal`](/reference/2026-01-01/objects/creategoalpayload)

[`deleteGoalPayload.goal`](/reference/2026-01-01/objects/deletegoalpayload)

[`updateGoalPayload.goal`](/reference/2026-01-01/objects/updategoalpayload)

[`Query.goal`](/reference/2026-01-01/queries/goal)

## Definition

```
"""
a goal
"""
type Goal {
  """
  Completion Percentage of a goal for a given date range. start_range/end_range should be of the form: 'yyyy-mm-dd'
  """
  completion_percentage_for_range(
    """
    The end of the date range.
    """
    end_range: String


    """
    The start of the date range.
    """
    start_range: String!
  ): Int


  """
  The rate at which this goal is completed
  """
  completion_rate: String
    @deprecated(reason: "should use completion_percentage_for_range")


  """
  The creation timestamp of the goal
  """
  created_at: ISO8601DateTime!


  """
  User who created this goal
  """
  created_user: User


  """
  created user of goal
  """
  created_user_id: ID


  """
  description of goal
  """
  description: String


  """
  due date of goal
  """
  due_date: ISO8601Date


  """
  All goal histories associated with this goal histories.
  """
  goal_histories: [GoalHistory!]!


  """
  The unique identifier of the goal
  """
  id: ID!


  """
  If true, the goal is complete for the given day. date should be of the form: 'yyyy-mm-dd'
  """
  is_completed_for_date(
    """
    The date to check if the goal is completed at that time.
    """
    date: String!
  ): Boolean


  """
  if true, the goal is currently active
  """
  is_current: Boolean
    @deprecated(
      reason: "should use is_completed_for_date field to determine if a goal is completed for a given day"
    )


  """
  if true, a template has been created based off this goal
  """
  is_used_as_template: Boolean


  """
  name of goal
  """
  name: String


  """
  parent id
  """
  parent_id: ID


  """
  The rate at which the parent goal has subgoals completed
  """
  parent_subgoal_completion_rate: String


  """
  Reminder object for a given goal
  """
  reminder: Reminder


  """
  frequency of goal
  """
  repeat: String


  """
  The id of the template used to make this goal
  """
  source_template_id: String


  """
  start date of goal
  """
  start_on: ISO8601Date!


  """
  Streak info for goal
  """
  streak_info(
    """
    The end of the date range.
    """
    end_range: String


    """
    The start of the date range.
    """
    start_range: String!
  ): [GoalStreakInfo!]


  """
  The rate at which a subgoal is completed
  """
  subgoal_completion_rate: String
    @deprecated(reason: "should use completion_percentage_for_range")


  """
  Subgoals for a given goal
  """
  subgoals: [Goal!]


  """
  count of subgoals
  """
  subgoals_count: String


  """
  Title hyperlink. Opens when the title is clicked on.
  """
  title_link: String


  """
  Owner of this goal
  """
  user: User


  """
  user id of goal
  """
  user_id: ID
}
```
