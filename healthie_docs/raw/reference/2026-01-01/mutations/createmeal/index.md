---
title: createMeal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmeal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createmeal/index.md
---

Create a Meal

## Arguments

[`input` ](#argument-input)· [`createMealInput` ](/reference/2026-01-01/input-objects/createmealinput)· Parameters for createMeal

## Returns

[`createMealPayload`](/reference/2026-01-01/objects/createmealpayload)

## Example

```
mutation createMeal($input: createMealInput) {
  createMeal(input: $input) {
    meal
    messages
  }
}
```
