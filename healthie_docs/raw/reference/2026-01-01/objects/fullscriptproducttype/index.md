---
title: FullscriptProductType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscriptproducttype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscriptproducttype/index.md
---

Fullscript Product Type

## Fields

[`additional_info` ](#field-additional-info)· [`String` ](/reference/2026-01-01/scalars/string)· Additional Info

[`dosage` ](#field-dosage)· [`String` ](/reference/2026-01-01/scalars/string)· Dosage of the product

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the product fullscript

[`ordered` ](#field-ordered)· [`String` ](/reference/2026-01-01/scalars/string)· Ordered

[`product_name` ](#field-product-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the product

## Used By

[`FullscriptTreatmentPlanType.recommendations`](/reference/2026-01-01/objects/fullscripttreatmentplantype)

## Definition

```
"""
Fullscript Product Type
"""
type FullscriptProductType {
  """
  Additional Info
  """
  additional_info: String


  """
  Dosage of the product
  """
  dosage: String


  """
  The unique identifier of the product fullscript
  """
  id: String!


  """
  Ordered
  """
  ordered: String


  """
  The name of the product
  """
  product_name: String
}
```
