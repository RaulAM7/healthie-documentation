---
title: deleteProduct | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteproduct/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/deleteproduct/index.md
---

Delete a product

## Arguments

[`input` ](#argument-input)· [`deleteProductInput` ](/reference/2026-01-01/input-objects/deleteproductinput)· Parameters for deleteProduct

## Returns

[`deleteProductPayload`](/reference/2026-01-01/objects/deleteproductpayload)

## Example

```
mutation deleteProduct($input: deleteProductInput) {
  deleteProduct(input: $input) {
    messages
    product
  }
}
```
