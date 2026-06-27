---
title: FullscriptPractitionerTypeType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscriptpractitionertypetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscriptpractitionertypetype/index.md
---

The type of practitioners

## Fields

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The code for the practitioner type

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the practitioner type

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the practitioner type

## Used By

[`Query.fullscriptPractitionerTypes`](/reference/2026-01-01/queries/fullscriptpractitionertypes)

## Definition

```
"""
The type of practitioners
"""
type FullscriptPractitionerTypeType {
  """
  The code for the practitioner type
  """
  code: String


  """
  The description of the practitioner type
  """
  description: String


  """
  The unique identifier of the practitioner type
  """
  id: String!
}
```
