---
title: allergySuggestions | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/queries/allergysuggestions/index
  md: https://docs.gethealthie.com/reference/2026-01-01/queries/allergysuggestions/index.md
---

Search results for allergies, allergens, and reactions

## Arguments

[`category` ](#argument-category)· [`String` ](/reference/2026-01-01/scalars/string)· accepts drug, environmental, food, pet, and reaction

## Returns

[`[String]`](/reference/2026-01-01/scalars/string)

## Example

```
query allergySuggestions($category: String) {
  allergySuggestions(category: $category)
}
```
