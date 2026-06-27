---
title: HealthReport | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/healthreport/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/healthreport/index.md
---

Health Report is a sub category of a HealthAssessment

## Fields

[`cancer` ](#field-cancer)· [`String` ](/reference/2026-01-01/scalars/string)· cancer of user

[`diabetes` ](#field-diabetes)· [`String` ](/reference/2026-01-01/scalars/string)· diabetes of user

[`fit_score` ](#field-fit-score)· [`String` ](/reference/2026-01-01/scalars/string)· The fit score of the user

[`heart` ](#field-heart)· [`String` ](/reference/2026-01-01/scalars/string)· lean\_body\_mass of user

[`respiratory` ](#field-respiratory)· [`String` ](/reference/2026-01-01/scalars/string)· respiratory of user

[`stroke` ](#field-stroke)· [`String` ](/reference/2026-01-01/scalars/string)· stroke of user

## Used By

[`HealthAssessment.health_report`](/reference/2026-01-01/objects/healthassessment)

## Definition

```
"""
Health Report is a sub category of a HealthAssessment
"""
type HealthReport {
  """
  cancer of user
  """
  cancer: String


  """
  diabetes of user
  """
  diabetes: String


  """
  The fit score of the user
  """
  fit_score: String


  """
  lean_body_mass of user
  """
  heart: String


  """
  respiratory of user
  """
  respiratory: String


  """
  stroke of user
  """
  stroke: String
}
```
