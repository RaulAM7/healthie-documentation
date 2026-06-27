---
title: Recommendation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/recommendation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/recommendation/index.md
---

A Care Plan Recommendation

## Fields

[`care_plan_recommendation_category` ](#field-care-plan-recommendation-category)· [`CarePlanRecommendationCategory` ](/reference/2026-01-01/objects/careplanrecommendationcategory)· The category of the recommendation

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the recommendation

[`recommendation_body` ](#field-recommendation-body)· [`String` ](/reference/2026-01-01/scalars/string)· Recommendation text

[`recommendation_type` ](#field-recommendation-type)· [`String` ](/reference/2026-01-01/scalars/string)· The type of recommendation (1)Activity, (2)Nutrition, (3)Supplement, (4)Other

[`sanitized_body` ](#field-sanitized-body)· [`String` ](/reference/2026-01-01/scalars/string)· Sanitized recommendation\_body

## Used By

[`CarePlan.recommendations`](/reference/2026-01-01/objects/careplan)

[`createRecommendationPayload.recommendation`](/reference/2026-01-01/objects/createrecommendationpayload)

[`deleteRecommendationPayload.recommendation`](/reference/2026-01-01/objects/deleterecommendationpayload)

[`updateRecommendationPayload.recommendation`](/reference/2026-01-01/objects/updaterecommendationpayload)

## Definition

```
"""
A Care Plan Recommendation
"""
type Recommendation {
  """
  The category of the recommendation
  """
  care_plan_recommendation_category: CarePlanRecommendationCategory


  """
  The unique identifier of the recommendation
  """
  id: ID!


  """
  Recommendation text
  """
  recommendation_body: String


  """
  The type of recommendation (1)Activity, (2)Nutrition, (3)Supplement, (4)Other
  """
  recommendation_type: String


  """
  Sanitized recommendation_body
  """
  sanitized_body: String
}
```
