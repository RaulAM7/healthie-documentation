---
title: OfferingProductInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/offeringproductinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/offeringproductinput/index.md
---

Payload for an offering product

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the offering product will be deleted

[`deduct_main_quantity` ](#field-deduct-main-quantity)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the main quantity will be deducted

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The ID of the offering product

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· The price of the offering product

[`product` ](#field-product)· [`ProductInput` ](/reference/2026-01-01/input-objects/productinput)· The offering product

[`quantity` ](#field-quantity)· [`Int` ](/reference/2026-01-01/scalars/int)· The quantity of the offering product

[`taxable` ](#field-taxable)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the offering product is taxable

## Used By

[`createOfferingInput.offering_products`](/reference/2026-01-01/input-objects/createofferinginput)

[`updateOfferingInput.offering_products`](/reference/2026-01-01/input-objects/updateofferinginput)

## Definition

```
"""
Payload for an offering product
"""
input OfferingProductInput {
  """
  If true, the offering product will be deleted
  """
  _destroy: Boolean


  """
  If true, the main quantity will be deducted
  """
  deduct_main_quantity: Boolean


  """
  The ID of the offering product
  """
  id: ID


  """
  The price of the offering product
  """
  price: String


  """
  The offering product
  """
  product: ProductInput


  """
  The quantity of the offering product
  """
  quantity: Int


  """
  If true, the offering product is taxable
  """
  taxable: Boolean
}
```
