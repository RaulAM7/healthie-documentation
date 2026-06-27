---
title: updateCarePlanRecommendationCategory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecareplanrecommendationcategory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecareplanrecommendationcategory/index.md
---

## Arguments

[`input` ](#argument-input)· [`updateCarePlanRecommendationCategoryInput` ](/reference/2026-01-01/input-objects/updatecareplanrecommendationcategoryinput)· Parameters for updateCarePlanRecommendationCategory

## Returns

[`updateCarePlanRecommendationCategoryPayload`](/reference/2026-01-01/objects/updatecareplanrecommendationcategorypayload)

## Example

```
mutation updateCarePlanRecommendationCategory(
  $input: updateCarePlanRecommendationCategoryInput
) {
  updateCarePlanRecommendationCategory(input: $input) {
    care_plan_recommendation_category
    messages
    organization
  }
}
```
