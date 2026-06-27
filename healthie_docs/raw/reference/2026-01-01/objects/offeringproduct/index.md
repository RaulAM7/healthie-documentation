---
title: OfferingProduct | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringproduct/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/offeringproduct/index.md
---

Offering product type

## Fields

[`deduct_main_quantity` ](#field-deduct-main-quantity)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true the quantity of the main product will be reduced, otherwise changing offering\_product.quantity won't affect on the main product

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the offering product

[`offering_id` ](#field-offering-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · ID of related offering

[`price` ](#field-price)· [`String` ](/reference/2026-01-01/scalars/string)· The price of included product. If offering\_product.price == nil, the price will be equal to product.price

[`product` ](#field-product)· [`Product` ](/reference/2026-01-01/objects/product)· A product included into the offering

[`quantity` ](#field-quantity)· [`Int` ](/reference/2026-01-01/scalars/int)· The quantity of included products

[`tax_amount` ](#field-tax-amount)· [`String` ](/reference/2026-01-01/scalars/string)· Tax amount if product has tax rate

[`taxable` ](#field-taxable)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If true tax will be added to the price

## Used By

[`Offering.offering_products`](/reference/2026-01-01/objects/offering)

## Definition

```
"""
Offering product type
"""
type OfferingProduct {
  """
  If true the quantity of the main product will be reduced, otherwise changing offering_product.quantity won't affect on the main product
  """
  deduct_main_quantity: Boolean


  """
  The unique identifier of the offering product
  """
  id: ID!


  """
  ID of related offering
  """
  offering_id: ID!


  """
  The price of included product. If offering_product.price == nil, the price will be equal to product.price
  """
  price: String


  """
  A product included into the offering
  """
  product: Product


  """
  The quantity of included products
  """
  quantity: Int


  """
  Tax amount if product has tax rate
  """
  tax_amount: String


  """
  If true tax will be added to the price
  """
  taxable: Boolean!
}
```
