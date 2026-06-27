---
title: HealthAssessment | Healthie API Docs
source_url:
  html: https://docs.gethealthie.com/reference/2026-01-01/objects/healthassessment/index
  md: https://docs.gethealthie.com/reference/2026-01-01/objects/healthassessment/index.md
---

Health Assessment contains in-depth help info and goals for a client

## Fields

[`body_report` ](#field-body-report)· [`BodyReport` ](/reference/2026-01-01/objects/bodyreport)· The body report for the client

[`created_at` ](#field-created-at)· [`ISO8601DateTime!` ](/reference/2026-01-01/scalars/iso8601datetime)· required · The date the health assessment was created

[`gender` ](#field-gender)· [`String` ](/reference/2026-01-01/scalars/string)· gen

[`health_report` ](#field-health-report)· [`HealthReport` ](/reference/2026-01-01/objects/healthreport)· The health report for the client

[`height` ](#field-height)· [`String` ](/reference/2026-01-01/scalars/string)· The height of the client

[`id` ](#field-id)· [`ID!` ](/reference/2026-01-01/scalars/id)· required · The unique identifier of the health accessment

[`is_diabetic` ](#field-is-diabetic)· [`Boolean` ](/reference/2026-01-01/scalars/boolean)· Is the client diabetic?

[`race` ](#field-race)· [`String` ](/reference/2026-01-01/scalars/string)· The race of the client

[`recommendation` ](#field-recommendation)· [`HealthAssessmentRecommendation` ](/reference/2026-01-01/objects/healthassessmentrecommendation)· The recommendation for the client

[`title` ](#field-title)· [`String` ](/reference/2026-01-01/scalars/string)· The title of the health assessment

## Used By

[`Query.healthAssessment`](/reference/2026-01-01/queries/healthassessment)

[`Query.healthAssessments`](/reference/2026-01-01/queries/healthassessments)

[`UpdateCalorieLevelPayload.assessment`](/reference/2026-01-01/objects/updatecalorielevelpayload)

[`UpdateMacronutrientSplitPayload.assessment`](/reference/2026-01-01/objects/updatemacronutrientsplitpayload)

## Definition

```
"""
Health Assessment contains in-depth help info and goals for a client
"""
type HealthAssessment {
  """
  The body report for the client
  """
  body_report: BodyReport


  """
  The date the health assessment was created
  """
  created_at: ISO8601DateTime!


  """
  gen
  """
  gender: String


  """
  The health report for the client
  """
  health_report: HealthReport


  """
  The height of the client
  """
  height: String


  """
  The unique identifier of the health accessment
  """
  id: ID!


  """
  Is the client diabetic?
  """
  is_diabetic: Boolean


  """
  The race of the client
  """
  race: String


  """
  The recommendation for the client
  """
  recommendation: HealthAssessmentRecommendation


  """
  The title of the health assessment
  """
  title: String
}
```
