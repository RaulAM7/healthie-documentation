---
title: Profession | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/profession/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/profession/index.md
---

Profession

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · Unique identifier of the profession

[`profession` ](#field-profession)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the profession

[`profession_category` ](#field-profession-category)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The category of the profession

## Used By

[`User.professions`](/reference/2026-01-01/objects/user)

## Definition

```
"""
Profession
"""
type Profession {
  """
  Unique identifier of the profession
  """
  id: ID!


  """
  The name of the profession
  """
  profession: String!


  """
  The category of the profession
  """
  profession_category: String!
}
```
