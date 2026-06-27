---
title: Benefit | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/benefit/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/benefit/index.md
---

Benefit associated with policy

## Fields

[`category` ](#field-category)· [`String` ](/reference/2026-01-01/scalars/string)· Enumerated field: Medical or Preventive. Describes the type of benefit

[`coinsurance` ](#field-coinsurance)· [`String` ](/reference/2026-01-01/scalars/string)· Coinsurance percentage due

[`copay` ](#field-copay)· [`String` ](/reference/2026-01-01/scalars/string)· Copay amount due

[`deductible_calendar_year` ](#field-deductible-calendar-year)· [`String` ](/reference/2026-01-01/scalars/string)· Deductible amount for the calendar year

[`deductible_year_to_date` ](#field-deductible-year-to-date)· [`String` ](/reference/2026-01-01/scalars/string)· Deductible amount for the year to date

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the benefit

[`metadata` ](#field-metadata)· [`JSON` ](/reference/2026-01-01/scalars/json)· A serialized JSON string of metadata. Maximum character limit of 2,000.

[`telemedicine` ](#field-telemedicine)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· If true, benefits include telemedicine

## Used By

[`Policy.benefits`](/reference/2026-01-01/objects/policy)

## Definition

```
"""
Benefit associated with policy
"""
type Benefit {
  """
  Enumerated field: Medical or Preventive. Describes the type of benefit
  """
  category: String


  """
  Coinsurance percentage due
  """
  coinsurance: String


  """
  Copay amount due
  """
  copay: String


  """
  Deductible amount for the calendar year
  """
  deductible_calendar_year: String


  """
  Deductible amount for the year to date
  """
  deductible_year_to_date: String


  """
  The unique identifier of the benefit
  """
  id: ID!


  """
  A serialized JSON string of metadata. Maximum character limit of 2,000.
  """
  metadata: JSON


  """
  If true, benefits include telemedicine
  """
  telemedicine: Boolean
}
```
