---
title: MealPlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/mealplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/mealplan/index.md
---

A meal plan

## Fields

[`active` ](#field-active)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, meal plan is active (most recent) on client's Living Plate account

[`date_added` ](#field-date-added)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date meal plan was added to client's Living Plate account

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the plan

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· name of the meal plan on Living Plate

[`offering_name` ](#field-offering-name)· [`String` ](/reference/2026-01-01/scalars/string)· If one exists, name of offering that was purchased that added meal plan to client's Living Plate account

## Used By

[`Offering.meal_plan_options`](/reference/2026-01-01/objects/offering)

[`User.purchased_meal_plans`](/reference/2026-01-01/objects/user)

[`Query.meal_plan_options`](/reference/2026-01-01/queries/meal-plan-options)

## Definition

```
"""
A meal plan
"""
type MealPlan {
  """
  If true, meal plan is active (most recent) on client's Living Plate account
  """
  active: Boolean


  """
  Date meal plan was added to client's Living Plate account
  """
  date_added: ISO8601DateTime


  """
  The unique identifier of the plan
  """
  id: ID!


  """
  name of the meal plan on Living Plate
  """
  name: String


  """
  If one exists, name of offering that was purchased that added meal plan to client's Living Plate account
  """
  offering_name: String
}
```
