---
title: FullscriptPractitionerType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscriptpractitionertype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/fullscriptpractitionertype/index.md
---

Fullscript Practitioner

## Fields

[`email` ](#field-email)· [`String` ](/reference/2026-01-01/scalars/string)· Email address of the practitioner

[`external_ref` ](#field-external-ref)· [`String` ](/reference/2026-01-01/scalars/string)· External reference of the practitioner

[`first_name` ](#field-first-name)· [`String` ](/reference/2026-01-01/scalars/string)· First name of the practitioner

[`id` ](#field-id)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The unique identifier of the practitioner

[`last_name` ](#field-last-name)· [`String` ](/reference/2026-01-01/scalars/string)· Last name of the practitioner

[`practitioner_type_id` ](#field-practitioner-type-id)· [`String` ](/reference/2026-01-01/scalars/string)· The ID of the practitioner type

## Used By

[`Query.fullscriptPractitioners`](/reference/2026-01-01/queries/fullscriptpractitioners)

[`createFullscriptPractitionerPayload.fullscript_practitioner`](/reference/2026-01-01/objects/createfullscriptpractitionerpayload)

## Definition

```
"""
Fullscript Practitioner
"""
type FullscriptPractitionerType {
  """
  Email address of the practitioner
  """
  email: String


  """
  External reference of the practitioner
  """
  external_ref: String


  """
  First name of the practitioner
  """
  first_name: String


  """
  The unique identifier of the practitioner
  """
  id: String!


  """
  Last name of the practitioner
  """
  last_name: String


  """
  The ID of the practitioner type
  """
  practitioner_type_id: String
}
```
