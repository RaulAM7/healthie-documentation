---
title: CarePlanRecommendationCategory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanrecommendationcategory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/careplanrecommendationcategory/index.md
---

A Care Plan Recommendation Category object

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

[`is_active` ](#field-is-active)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required

[`is_editable` ](#field-is-editable)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required

[`organization` ](#field-organization)· [`Organization!` ](/reference/2026-01-01/objects/organization)· required

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required

## Used By

[`Organization.care_plan_recommendation_categories`](/reference/2026-01-01/objects/organization)

[`Recommendation.care_plan_recommendation_category`](/reference/2026-01-01/objects/recommendation)

[`createCarePlanRecommendationCategoryPayload.care_plan_recommendation_category`](/reference/2026-01-01/objects/createcareplanrecommendationcategorypayload)

[`deleteCarePlanRecommendationCategoryPayload.care_plan_recommendation_category`](/reference/2026-01-01/objects/deletecareplanrecommendationcategorypayload)

[`updateCarePlanRecommendationCategoryPayload.care_plan_recommendation_category`](/reference/2026-01-01/objects/updatecareplanrecommendationcategorypayload)

## Definition

```
"""
A Care Plan Recommendation Category object
"""
type CarePlanRecommendationCategory {
  created_at: ISO8601DateTime!
  id: ID!
  is_active: Boolean!
  is_editable: Boolean!
  name: String!
  organization: Organization!
  updated_at: ISO8601DateTime!
}
```
