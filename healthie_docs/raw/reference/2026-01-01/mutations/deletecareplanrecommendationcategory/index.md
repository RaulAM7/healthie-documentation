---
title: deleteCarePlanRecommendationCategory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecareplanrecommendationcategory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecareplanrecommendationcategory/index.md
---

## Arguments

[`input` ](#argument-input)· [`deleteCarePlanRecommendationCategoryInput` ](/reference/2026-01-01/input-objects/deletecareplanrecommendationcategoryinput)· Parameters for deleteCarePlanRecommendationCategory

## Returns

[`deleteCarePlanRecommendationCategoryPayload`](/reference/2026-01-01/objects/deletecareplanrecommendationcategorypayload)

## Example

```
mutation deleteCarePlanRecommendationCategory(
  $input: deleteCarePlanRecommendationCategoryInput
) {
  deleteCarePlanRecommendationCategory(input: $input) {
    care_plan_recommendation_category
    messages
    organization
  }
}
```
