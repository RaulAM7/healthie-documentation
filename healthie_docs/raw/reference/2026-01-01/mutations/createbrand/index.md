---
title: createBrand | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/mutations/createbrand/index
  md: https://docs.gethealthie.com/reference/2026-01-01/mutations/createbrand/index.md
---

create Brand

## Arguments

[`input` ](#argument-input)· [`createBrandInput` ](/reference/2026-01-01/input-objects/createbrandinput)· Parameters for createBrand

## Returns

[`createBrandPayload`](/reference/2026-01-01/objects/createbrandpayload)

## Example

```
mutation createBrand($input: createBrandInput) {
  createBrand(input: $input) {
    brand
    messages
  }
}
```
