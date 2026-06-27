---
title: updateRecommendation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updaterecommendation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updaterecommendation/index.md
---

Update a care plan recommendation

## Arguments

[`input` ](#argument-input)· [`updateRecommendationInput` ](/reference/2026-01-01/input-objects/updaterecommendationinput)· Parameters for updateRecommendation

## Returns

[`updateRecommendationPayload`](/reference/2026-01-01/objects/updaterecommendationpayload)

## Example

```
mutation updateRecommendation($input: updateRecommendationInput) {
  updateRecommendation(input: $input) {
    messages
    recommendation
  }
}
```
