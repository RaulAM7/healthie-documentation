---
title: BodyReport | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/bodyreport/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/bodyreport/index.md
---

Body Report is a sub category of a HealthAssessment

## Fields

[`amr` ](#field-amr)· [`String` ](/reference/2026-01-01/scalars/string)· amr of user

[`bmi` ](#field-bmi)· [`String` ](/reference/2026-01-01/scalars/string)· bmi of user

[`body_fat_percent` ](#field-body-fat-percent)· [`String` ](/reference/2026-01-01/scalars/string)· body\_fat\_percent of user

[`body_weight` ](#field-body-weight)· [`String` ](/reference/2026-01-01/scalars/string)· body\_weight of user

[`c_bmi` ](#field-c-bmi)· [`String` ](/reference/2026-01-01/scalars/string)· c\_bmi of user

[`fat_mass` ](#field-fat-mass)· [`String` ](/reference/2026-01-01/scalars/string)· fat\_mass of user

[`lean_body_mass` ](#field-lean-body-mass)· [`String` ](/reference/2026-01-01/scalars/string)· lean\_body\_mass of user

[`rmr` ](#field-rmr)· [`String` ](/reference/2026-01-01/scalars/string)· rmr of user

## Used By

[`HealthAssessment.body_report`](/reference/2026-01-01/objects/healthassessment)

## Definition

```
"""
Body Report is a sub category of a HealthAssessment
"""
type BodyReport {
  """
  amr of user
  """
  amr: String


  """
  bmi of user
  """
  bmi: String


  """
  body_fat_percent of user
  """
  body_fat_percent: String


  """
  body_weight of user
  """
  body_weight: String


  """
  c_bmi of user
  """
  c_bmi: String


  """
  fat_mass of user
  """
  fat_mass: String


  """
  lean_body_mass of user
  """
  lean_body_mass: String


  """
  rmr of user
  """
  rmr: String
}
```
