---
title: BenefitInput | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/input-objects/benefitinput/index
  md: https://docs.gethealthie.com/reference/2026-01-01/input-objects/benefitinput/index.md
---

Payload for a benefit

## Fields

[`_destroy` ](#field--destroy)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, the benefit will be deleted

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· The category of the benefit

[`coinsurance` ](#field-coinsurance)· [`String` ](/reference/2026-01-01/scalars/string)· The coinsurance for the benefit

[`copay` ](#field-copay)· [`String` ](/reference/2026-01-01/scalars/string)· The copay for the benefit

[`deductible_calendar_year` ](#field-deductible-calendar-year)· [`String` ](/reference/2026-01-01/scalars/string)· The deductible calendar year for the benefit

[`deductible_year_to_date` ](#field-deductible-year-to-date)· [`String` ](/reference/2026-01-01/scalars/string)· The deductible year to date for the benefit

[`id` ](#field-id)· [`ID` ](/reference/2026-01-01/scalars/id)· The id of the benefit

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`telemedicine` ](#field-telemedicine)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Whether or not the benefit covers telemedicine

## Used By

[`updatePolicyMutationInput.benefits`](/reference/2026-01-01/input-objects/updatepolicymutationinput)

## Definition

```
"""
Payload for a benefit
"""
input BenefitInput {
  """
  If true, the benefit will be deleted
  """
  _destroy: Boolean


  """
  The category of the benefit
  """
  category: String


  """
  The coinsurance for the benefit
  """
  coinsurance: String


  """
  The copay for the benefit
  """
  copay: String


  """
  The deductible calendar year for the benefit
  """
  deductible_calendar_year: String


  """
  The deductible year to date for the benefit
  """
  deductible_year_to_date: String


  """
  The id of the benefit
  """
  id: ID


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  Whether or not the benefit covers telemedicine
  """
  telemedicine: Boolean
}
```
