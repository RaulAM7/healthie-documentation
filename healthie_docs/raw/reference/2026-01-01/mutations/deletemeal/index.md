---
title: deleteMeal | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemeal/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletemeal/index.md
---

Destroy a Meal

## Arguments

[`input` ](#argument-input)· [`deleteMealInput` ](/reference/2026-01-01/input-objects/deletemealinput)· Parameters for deleteMeal

## Returns

[`deleteMealPayload`](/reference/2026-01-01/objects/deletemealpayload)

## Example

```
mutation deleteMeal($input: deleteMealInput) {
  deleteMeal(input: $input) {
    meal
    messages
  }
}
```
