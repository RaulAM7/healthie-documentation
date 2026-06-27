---
title: AllergySensitivity | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/allergysensitivity/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/allergysensitivity/index.md
---

An allergy/sensitivity/preference for a client

## Fields

[`category` ](#field-category)· [`AllergySensitivityCategory!` ](/reference/2026-01-01/enums/allergysensitivitycategory)· required · Enum field. Options: allergy, sensitivity, preference, intolerance, ccda

[`category_type` ](#field-category-type)· [`AllergySensitivityCategoryType` ](/reference/2026-01-01/enums/allergysensitivitycategorytype)· Type of allergy or like/dislike for preference. Options: food, drug, environmental, pet, latex, like, dislike

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · Date/Time created

[`created_by` ](#field-created-by)· [`User` ](/reference/2026-01-01/objects/user)· User who created this allergy

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the allergy

[`is_current` ](#field-is-current)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If the allergy is current.

deprecated

Use status instead

[`mirrored` ](#field-mirrored)· [`Boolean!` ](/reference/2026-01-01/scalars/boolean)· required · If the allergy is synchronized with an external system (e.g., an E-Rx system)

[`name` ](#field-name)· [`String` ](/reference/2026-01-01/scalars/string)· The name of the allergy/sensitivity/preference

[`onset_date` ](#field-onset-date)· [`ISO8601Date` ](/reference/2026-01-01/scalars/iso8601date)· The date of onset

[`reaction` ](#field-reaction)· [`String` ](/reference/2026-01-01/scalars/string)· Description of the reaction on the allergen

[`reaction_type` ](#field-reaction-type)· [`AllergySensitivityReactionType` ](/reference/2026-01-01/enums/allergysensitivityreactiontype)· The type of the reaction. Options are \[allergy, adverse\_reaction]

[`requires_consolidation` ](#field-requires-consolidation)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· When true, this object must be consolidated as part of a CCDA Ingest

[`severity` ](#field-severity)· [`AllergySensitivitySeverity` ](/reference/2026-01-01/enums/allergysensitivityseverity)· The severity of the allergy. Options: mild, moderate, severe, unknown

[`status` ](#field-status)· [`AllergySensitivityStatus` ](/reference/2026-01-01/enums/allergysensitivitystatus)· The allergy's current status. Options are \[active, inactive, resolved]

[`updated_at` ](#field-updated-at)· [`ISO8601DateTime` ](/reference/2026-01-01/scalars/iso8601datetime)· Date/Time last updated

## Used By

[`User.allergy_sensitivities`](/reference/2026-01-01/objects/user)

[`User.last_updated_allergy`](/reference/2026-01-01/objects/user)

[`createAllergySensitivityPayload.allergy_sensitivity`](/reference/2026-01-01/objects/createallergysensitivitypayload)

[`createAllergySensitivityPayload.duplicate_allergy`](/reference/2026-01-01/objects/createallergysensitivitypayload)

[`deleteAllergySensitivityPayload.allergy_sensitivity`](/reference/2026-01-01/objects/deleteallergysensitivitypayload)

[`updateAllergySensitivityPayload.allergy_sensitivity`](/reference/2026-01-01/objects/updateallergysensitivitypayload)

[`updateAllergySensitivityPayload.duplicate_allergy`](/reference/2026-01-01/objects/updateallergysensitivitypayload)

## Definition

```
"""
An allergy/sensitivity/preference for a client
"""
type AllergySensitivity {
  """
  Enum field. Options: allergy, sensitivity, preference, intolerance, ccda
  """
  category: AllergySensitivityCategory!


  """
  Type of allergy or like/dislike for preference. Options: food, drug, environmental, pet, latex, like, dislike
  """
  category_type: AllergySensitivityCategoryType


  """
  Date/Time created
  """
  created_at: ISO8601DateTime!


  """
  User who created this allergy
  """
  created_by: User


  """
  The unique identifier of the allergy
  """
  id: ID!


  """
  If the allergy is current.
  """
  is_current: Boolean @deprecated(reason: "Use status instead")


  """
  If the allergy is synchronized with an external system (e.g., an E-Rx system)
  """
  mirrored: Boolean!


  """
  The name of the allergy/sensitivity/preference
  """
  name: String


  """
  The date of onset
  """
  onset_date: ISO8601Date


  """
  Description of the reaction on the allergen
  """
  reaction: String


  """
  The type of the reaction. Options are [allergy, adverse_reaction]
  """
  reaction_type: AllergySensitivityReactionType


  """
  When true, this object must be consolidated as part of a CCDA Ingest
  """
  requires_consolidation: Boolean


  """
  The severity of the allergy. Options: mild, moderate, severe, unknown
  """
  severity: AllergySensitivitySeverity


  """
  The allergy's current status. Options are [active, inactive, resolved]
  """
  status: AllergySensitivityStatus


  """
  Date/Time last updated
  """
  updated_at: ISO8601DateTime
}
```
