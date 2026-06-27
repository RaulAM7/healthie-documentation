---
title: deleteCustomFood | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustomfood/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deletecustomfood/index.md
---

Destroy a Custom Food

## Arguments

[`input` ](#argument-input)· [`deleteCustomFoodInput` ](/reference/2026-01-01/input-objects/deletecustomfoodinput)· Parameters for deleteCustomFood

## Returns

[`deleteCustomFoodPayload`](/reference/2026-01-01/objects/deletecustomfoodpayload)

## Example

```
mutation deleteCustomFood($input: deleteCustomFoodInput) {
  deleteCustomFood(input: $input) {
    customFood
    messages
  }
}
```
