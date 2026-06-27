---
title: MedicationOptionType | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationoptiontype/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/medicationoptiontype/index.md
---

Medication query result

## Fields

[`dosage_options` ](#field-dosage-options)· [`[DosageType]` ](/reference/2026-01-01/objects/dosagetype)· The dosage options of the medication option

[`dosages` ](#field-dosages)· [`[String!]` ](/reference/2026-01-01/scalars/string)· The dosages of the medication option

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the medication option

[`monograph` ](#field-monograph)· [`String` ](/reference/2026-01-01/scalars/string)· The monograph of the medication option

[`name` ](#field-name)· [`String!` ](/reference/2026-01-01/scalars/string)· required · The name of the medication option

## Used By

[`Query.medication_option`](/reference/2026-01-01/queries/medication-option)

[`Query.medication_options`](/reference/2026-01-01/queries/medication-options)

## Definition

```
"""
Medication query result
"""
type MedicationOptionType {
  """
  The dosage options of the medication option
  """
  dosage_options: [DosageType]


  """
  The dosages of the medication option
  """
  dosages: [String!]


  """
  The unique identifier of the medication option
  """
  id: ID!


  """
  The monograph of the medication option
  """
  monograph(
    """
    The format of the monograph
    """
    format: MonographFormat = HTML
  ): String


  """
  The name of the medication option
  """
  name: String!
}
```
