---
title: DrugAllergenType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/drugallergentype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/drugallergentype/index.md
---

Allergen information

## Fields

[`brand_name` ](#field-brand-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The brand name of the allergen

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the allergen

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the allergen

[`type` ](#field-type)· [`DrugAllergenTypeEnum!` ](/reference/2026-01-01/enums/drugallergentypeenum)· required · The type of allergen

## Used By

[`Query.drugAllergen`](/reference/2026-01-01/queries/drugallergen)

[`Query.drugAllergens`](/reference/2026-01-01/queries/drugallergens)

## Definition

```
"""
Allergen information
"""
type DrugAllergenType {
  """
  The brand name of the allergen
  """
  brand_name: String!


  """
  The unique identifier of the allergen
  """
  id: ID!


  """
  The name of the allergen
  """
  name: String!


  """
  The type of allergen
  """
  type: DrugAllergenTypeEnum!
}
```
