---
title: StripePlan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/stripeplan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/stripeplan/index.md
---

A discount from stripe as object

## Fields

[`amount` ](#field-amount)· [`String` ](/reference/2026-01-01/scalars/string)· The amount in cents to be charged on the interval specified

[`annual_cost` ](#field-annual-cost)· [`String` ](/reference/2026-01-01/scalars/string)· The annual cost of the plan

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the plan

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the plan

[`interval` ](#field-interval)· [`String` ](/reference/2026-01-01/scalars/string)· The interval when the plan is charged

## Used By

[`StripeInvoice.add_ons`](/reference/2026-01-01/objects/stripeinvoice)

[`StripeInvoice.applied_balance`](/reference/2026-01-01/objects/stripeinvoice)

[`StripeInvoice.base_plan`](/reference/2026-01-01/objects/stripeinvoice)

[`StripeInvoice.credits`](/reference/2026-01-01/objects/stripeinvoice)

[`SubscriptionInstance.plan_add_ons`](/reference/2026-01-01/objects/subscriptioninstance)

## Definition

```
"""
A discount from stripe as object
"""
type StripePlan {
  """
  The amount in cents to be charged on the interval specified
  """
  amount: String


  """
  The annual cost of the plan
  """
  annual_cost: String


  """
  The description of the plan
  """
  description: String


  """
  The unique identifier of the plan
  """
  id: String!


  """
  The interval when the plan is charged
  """
  interval: String
}
```
