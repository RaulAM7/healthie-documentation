---
title: updateCalorieLevel | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecalorielevel/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecalorielevel/index.md
---

deprecated Deprecated, do not use

Update Calorie Levels in the Health Assessment Service

## Arguments

[`input` ](#argument-input)· [`UpdateCalorieLevelInput` ](/reference/2026-01-01/input-objects/updatecalorielevelinput)· Parameters for UpdateCalorieLevel

## Returns

[`UpdateCalorieLevelPayload`](/reference/2026-01-01/objects/updatecalorielevelpayload)

## Example

```
mutation updateCalorieLevel($input: UpdateCalorieLevelInput) {
  updateCalorieLevel(input: $input) {
    assessment
    messages
  }
}
```
