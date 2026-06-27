---
title: createCustomFood | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustomfood/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createcustomfood/index.md
---

Create a Custom Food

## Arguments

[`input` ](#argument-input)· [`createCustomFoodInput` ](/reference/2026-01-01/input-objects/createcustomfoodinput)· Parameters for createCustomFood

## Returns

[`createCustomFoodPayload`](/reference/2026-01-01/objects/createcustomfoodpayload)

## Example

```
mutation createCustomFood($input: createCustomFoodInput) {
  createCustomFood(input: $input) {
    customFood
    messages
  }
}
```
