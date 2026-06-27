---
title: DosageType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/dosagetype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/dosagetype/index.md
---

Dosage of a medication or prescription

## Fields

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the dosage

[`ndc` ](#field-ndc)· [`String` ](/reference/2026-01-01/scalars/string)· The medication's national drug code

[`strength` ](#field-strength)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The strength of the dosage

## Used By

[`MedicationOptionType.dosage_options`](/reference/2026-01-01/objects/medicationoptiontype)

## Definition

```
"""
Dosage of a medication or prescription
"""
type DosageType {
  """
  The unique identifier of the dosage
  """
  id: ID!


  """
  The medication's national drug code
  """
  ndc: String


  """
  The strength of the dosage
  """
  strength: String!
}
```
