---
title: ProductInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/productinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/productinput/index.md
---

Product input

## Fields

[`id` ](#field-id)· [`String` ](/reference/2026-01-01/scalars/string)· The product id

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The product name

## Used By

[`OfferingProductInput.product`](/reference/2026-01-01/input-objects/offeringproductinput)

## Definition

```
"""
Product input
"""
input ProductInput {
  """
  The product id
  """
  id: String


  """
  The product name
  """
  name: String
}
```
