---
title: GoalTemplate | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/goaltemplate/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/goaltemplate/index.md
---

a goal template

## Fields

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· description of template from associated goal

[`goal_id` ](#field-goal-id)· [`String` ](/reference/2026-01-01/scalars/string)· id of the goal this template was based on

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · id of the the relevant goal template

[`is_healthie_default` ](#field-is-healthie-default)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · is\_healthie\_default of the the relevant goal template

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of template from associated goal

[`repeat` ](#field-repeat)· [`String!` ](/reference/2026-01-01/scalars/string)· required · frequency of template from associated goal

[`subgoal_templates` ](#field-subgoal-templates)· [`[GoalTemplate!]` ](/reference/2026-01-01/objects/goaltemplate)· Subgoal templates for a given template

[`title_link` ](#field-title-link)· [`String` ](/reference/2026-01-01/scalars/string)· Title hyperlink. Opens when the title is clicked on.

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· user associated with this template

[`user_id` ](#field-user-id)· [`String` ](/reference/2026-01-01/scalars/string)· user who owns this goal template

## Used By

[`GoalTemplate.subgoal_templates`](/reference/2026-01-01/objects/goaltemplate)

[`GoalTemplateEdge.node`](/reference/2026-01-01/objects/goaltemplateedge)

[`GoalTemplatePaginationConnection.nodes`](/reference/2026-01-01/objects/goaltemplatepaginationconnection)

## Definition

```
"""
a goal template
"""
type GoalTemplate {
  """
  description of template from associated goal
  """
  description: String


  """
  id of the goal this template was based on
  """
  goal_id: String


  """
  id of the the relevant goal template
  """
  id: String!


  """
  is_healthie_default of the the relevant goal template
  """
  is_healthie_default: Boolean!


  """
  name of template from associated goal
  """
  name: String


  """
  frequency of template from associated goal
  """
  repeat: String!


  """
  Subgoal templates for a given template
  """
  subgoal_templates: [GoalTemplate!]


  """
  Title hyperlink. Opens when the title is clicked on.
  """
  title_link: String


  """
  user associated with this template
  """
  user: User


  """
  user who owns this goal template
  """
  user_id: String
}
```
