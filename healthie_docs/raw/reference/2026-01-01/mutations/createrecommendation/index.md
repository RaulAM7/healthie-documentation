---
title: createRecommendation | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrecommendation/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createrecommendation/index.md
---

Create a care plan recommendation

## Arguments

[`input` ](#argument-input)· [`createRecommendationInput` ](/reference/2026-01-01/input-objects/createrecommendationinput)· Parameters for createRecommendation

## Returns

[`createRecommendationPayload`](/reference/2026-01-01/objects/createrecommendationpayload)

## Example

```
mutation createRecommendation($input: createRecommendationInput) {
  createRecommendation(input: $input) {
    messages
    recommendation
  }
}
```
