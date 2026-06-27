---
title: drugAllergen | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/drugallergen/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/drugallergen/index.md
---

Fetch an allergen by ID

## Arguments

[`id` ](#argument-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required

## Returns

[`DrugAllergenType`](/reference/2026-01-01/objects/drugallergentype)

## Example

```
query drugAllergen($id: ID!) {
  drugAllergen(id: $id) {
    brand_name
    id
    name
    type
  }
}
```
