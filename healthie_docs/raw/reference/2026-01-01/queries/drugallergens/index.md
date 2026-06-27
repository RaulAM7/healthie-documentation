---
title: drugAllergens | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/drugallergens/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/drugallergens/index.md
---

Search for allergens by name

## Arguments

[`keywords` ](#argument-keywords)· [`String!` ](/reference/2026-01-01/scalars/string)· required

## Returns

[`[DrugAllergenType!]`](/reference/2026-01-01/objects/drugallergentype)

## Example

```
query drugAllergens($keywords: String!) {
  drugAllergens(keywords: $keywords) {
    brand_name
    id
    name
    type
  }
}
```
