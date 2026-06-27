---
title: updateCustomFood | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustomfood/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatecustomfood/index.md
---

Update a Custom Food

## Arguments

[`input` ](#argument-input)· [`updateCustomFoodInput` ](/reference/2026-01-01/input-objects/updatecustomfoodinput)· Parameters for updateCustomFood

## Returns

[`updateCustomFoodPayload`](/reference/2026-01-01/objects/updatecustomfoodpayload)

## Example

```
mutation updateCustomFood($input: updateCustomFoodInput) {
  updateCustomFood(input: $input) {
    customFood
    messages
  }
}
```
