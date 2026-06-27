---
title: Specialty | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/specialty/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/specialty/index.md
---

Specialty

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the specialty

[`specialty` ](#field-specialty)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the specialty

[`specialty_category` ](#field-specialty-category)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the specialty category

## Used By

[`User.specialties`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Specialty
"""
type Specialty {
  """
  The unique identifier of the specialty
  """
  id: ID!


  """
  The name of the specialty
  """
  specialty: String!


  """
  The name of the specialty category
  """
  specialty_category: String!
}
```
