---
title: updateMeal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemeal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatemeal/index.md
---

Update a Meal

## Arguments

[`input` ](#argument-input)· [`updateMealInput` ](/reference/2026-01-01/input-objects/updatemealinput)· Parameters for updateMeal

## Returns

[`updateMealPayload`](/reference/2026-01-01/objects/updatemealpayload)

## Example

```
mutation updateMeal($input: updateMealInput) {
  updateMeal(input: $input) {
    meal
    messages
  }
}
```
