---
title: deleteRecommendation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleterecommendation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleterecommendation/index.md
---

Destroy a care plan recommendation

## Arguments

[`input` ](#argument-input)· [`deleteRecommendationInput` ](/reference/2026-01-01/input-objects/deleterecommendationinput)· Parameters for deleteRecommendation

## Returns

[`deleteRecommendationPayload`](/reference/2026-01-01/objects/deleterecommendationpayload)

## Example

```
mutation deleteRecommendation($input: deleteRecommendationInput) {
  deleteRecommendation(input: $input) {
    messages
    recommendation
  }
}
```
