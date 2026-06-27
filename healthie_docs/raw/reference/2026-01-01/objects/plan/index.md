---
title: Plan | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/plan/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/plan/index.md
---

A plan that can be used for a subscription

## Fields

[`features` ](#field-features)· [`[String]` ](/reference/2026-01-01/scalars/string)· The features of the plan

[`header` ](#field-header)· [`String` ](/reference/2026-01-01/scalars/string)· The header of the plan

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the plan

[`subheader` ](#field-subheader)· [`String` ](/reference/2026-01-01/scalars/string)· The subheader of the plan

## Used By

[`Query.plan`](/reference/2026-01-01/queries/plan)

## Definition

```
"""
A plan that can be used for a subscription
"""
type Plan {
  """
  The features of the plan
  """
  features: [String]


  """
  The header of the plan
  """
  header: String


  """
  The unique identifier of the plan
  """
  id: ID!


  """
  The subheader of the plan
  """
  subheader: String
}
```
