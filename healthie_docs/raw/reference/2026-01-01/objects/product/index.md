---
title: Product | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/product/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/product/index.md
---

The product

## Fields

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date and time when the product was created

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the product

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the product

[`price` ](#field-price)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The price of the product

[`remaining_quantity` ](#field-remaining-quantity)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The available amount of the product

[`tax_description` ](#field-tax-description)· [`String` ](/reference/2026-01-01/scalars/string)· Tax description

[`tax_rate` ](#field-tax-rate)· [`String` ](/reference/2026-01-01/scalars/string)· Tax rate

[`taxable` ](#field-taxable)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If product has tax rate

[`unlimited_quantity` ](#field-unlimited-quantity)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · Indicates if the product has unlimited amount

[`user` ](#field-user)· [`User` ](/reference/2026-01-01/objects/user)· Owner of the product

## Used By

[`OfferingProduct.product`](/reference/2026-01-01/objects/offeringproduct)

[`ProductEdge.node`](/reference/2026-01-01/objects/productedge)

[`ProductPaginationConnection.nodes`](/reference/2026-01-01/objects/productpaginationconnection)

[`createProductPayload.product`](/reference/2026-01-01/objects/createproductpayload)

[`deleteProductPayload.product`](/reference/2026-01-01/objects/deleteproductpayload)

[`updateProductPayload.product`](/reference/2026-01-01/objects/updateproductpayload)

## Definition

```
"""
The product
"""
type Product {
  """
  The date and time when the product was created
  """
  created_at: ISO8601DateTime!


  """
  The unique identifier of the product
  """
  id: ID!


  """
  The name of the product
  """
  name: String!


  """
  The price of the product
  """
  price: String!


  """
  The available amount of the product
  """
  remaining_quantity: String!


  """
  Tax description
  """
  tax_description: String


  """
  Tax rate
  """
  tax_rate: String


  """
  If product has tax rate
  """
  taxable: Boolean


  """
  Indicates if the product has unlimited amount
  """
  unlimited_quantity: Boolean!


  """
  Owner of the product
  """
  user: User
}
```
