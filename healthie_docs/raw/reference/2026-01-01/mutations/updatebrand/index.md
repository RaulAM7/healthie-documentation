---
title: updateBrand | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatebrand/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/updatebrand/index.md
---

Update a Brand and return Brand

## Arguments

[`input` ](#argument-input)· [`updateBrandInput` ](/reference/2026-01-01/input-objects/updatebrandinput)· Parameters for updateBrand

## Returns

[`updateBrandPayload`](/reference/2026-01-01/objects/updatebrandpayload)

## Example

```
mutation updateBrand($input: updateBrandInput) {
  updateBrand(input: $input) {
    brand
    messages
  }
}
```
