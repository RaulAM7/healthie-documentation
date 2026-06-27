---
title: createProduct | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createproduct/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createproduct/index.md
---

Create a product

## Arguments

[`input` ](#argument-input)· [`createProductInput` ](/reference/2026-01-01/input-objects/createproductinput)· Parameters for createProduct

## Returns

[`createProductPayload`](/reference/2026-01-01/objects/createproductpayload)

## Example

```
mutation createProduct($input: createProductInput) {
  createProduct(input: $input) {
    messages
    product
  }
}
```
