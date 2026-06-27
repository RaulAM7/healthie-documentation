---
title: updateProduct | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateproduct/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updateproduct/index.md
---

Update a product

## Arguments

[`input` ](#argument-input)· [`updateProductInput` ](/reference/2026-01-01/input-objects/updateproductinput)· Parameters for updateProduct

## Returns

[`updateProductPayload`](/reference/2026-01-01/objects/updateproductpayload)

## Example

```
mutation updateProduct($input: updateProductInput) {
  updateProduct(input: $input) {
    messages
    product
  }
}
```
