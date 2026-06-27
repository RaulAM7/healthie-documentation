---
title: FullscriptTreatmentPlanType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscripttreatmentplantype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscripttreatmentplantype/index.md
---

Fullscript Treatment Plan

## Fields

[`activation_date` ](#field-activation-date)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date the treatment plan was activated

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the plan

[`ordered_count` ](#field-ordered-count)· [`Int` ](/reference/2026-01-01/scalars/int)· Number of times the plan has been ordered

[`personal_message` ](#field-personal-message)· [`String` ](/reference/2026-01-01/scalars/string)· Personal message from the practitioner

[`practitioner_name` ](#field-practitioner-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the practitioner

[`recommendations` ](#field-recommendations)· [`[FullscriptProductType!]` ](/reference/2026-01-01/objects/fullscriptproducttype)· The products recommended in the plan

## Used By

[`Query.treatmentPlans`](/reference/2026-01-01/queries/treatmentplans)

## Definition

```
"""
Fullscript Treatment Plan
"""
type FullscriptTreatmentPlanType {
  """
  Date the treatment plan was activated
  """
  activation_date: ISO8601DateTime


  """
  The unique identifier of the plan
  """
  id: String!


  """
  Number of times the plan has been ordered
  """
  ordered_count: Int


  """
  Personal message from the practitioner
  """
  personal_message: String


  """
  The name of the practitioner
  """
  practitioner_name: String


  """
  The products recommended in the plan
  """
  recommendations: [FullscriptProductType!]
}
```
