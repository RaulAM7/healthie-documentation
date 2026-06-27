---
title: CptCode | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcode/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/cptcode/index.md
---

The CPT code

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· The CPT code category

deprecated

Always returns nil

[`code` ](#field-code)· [`String` ](/reference/2026-01-01/scalars/string)· The CPT code

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date when the CPT code was created

[`description` ](#field-description)· [`String` ](/reference/2026-01-01/scalars/string)· The description of the CPT code

[`display_name` ](#field-display-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the CPT code for use in labels

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the CPT code

[`is_favorite` ](#field-is-favorite)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether a CPT code marked as favorite

[`last_fee` ](#field-last-fee)· [`Float` ](/reference/2026-01-01/scalars/float)· The last fee applied to this CPT code by a provider

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date when the CPT code was updated

## Used By

[`AppointmentPricingInfoType.cpt_code`](/reference/2026-01-01/objects/appointmentpricinginfotype)

[`CptCodeEdge.node`](/reference/2026-01-01/objects/cptcodeedge)

[`CptCodePaginationConnection.nodes`](/reference/2026-01-01/objects/cptcodepaginationconnection)

[`CptCodesCms1500.cpt_code`](/reference/2026-01-01/objects/cptcodescms1500)

[`CptCodesSuperBill.cpt_code`](/reference/2026-01-01/objects/cptcodessuperbill)

[`PreferredMedicalCode.cpt_code`](/reference/2026-01-01/objects/preferredmedicalcode)

## Definition

```
"""
The CPT code
"""
type CptCode {
  """
  The CPT code category
  """
  category: String @deprecated(reason: "Always returns nil")


  """
  The CPT code
  """
  code: String


  """
  The date when the CPT code was created
  """
  created_at: ISO8601DateTime!


  """
  The description of the CPT code
  """
  description: String


  """
  The name of the CPT code for use in labels
  """
  display_name: String


  """
  The unique identifier of the CPT code
  """
  id: ID!


  """
  Whether a CPT code marked as favorite
  """
  is_favorite(
    """
    The known value of is_favorite (from the query argument)
    """
    known_value: Boolean
  ): Boolean


  """
  The last fee applied to this CPT code by a provider
  """
  last_fee: Float


  """
  The date when the CPT code was updated
  """
  updated_at: ISO8601DateTime!
}
```
