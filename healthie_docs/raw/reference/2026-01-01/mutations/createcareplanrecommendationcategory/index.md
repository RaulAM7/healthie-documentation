---
title: createCarePlanRecommendationCategory | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcareplanrecommendationcategory/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcareplanrecommendationcategory/index.md
---

## Arguments

[`input` ](#argument-input)· [`createCarePlanRecommendationCategoryInput` ](/reference/2026-01-01/input-objects/createcareplanrecommendationcategoryinput)· Parameters for createCarePlanRecommendationCategory

## Returns

[`createCarePlanRecommendationCategoryPayload`](/reference/2026-01-01/objects/createcareplanrecommendationcategorypayload)

## Example

```
mutation createCarePlanRecommendationCategory(
  $input: createCarePlanRecommendationCategoryInput
) {
  createCarePlanRecommendationCategory(input: $input) {
    care_plan_recommendation_category
    messages
    organization
  }
}
```
